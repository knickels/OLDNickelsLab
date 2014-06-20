/* Copyright 2008 Renato Florentino Garcia <fgar.renato@gmail.com>
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License version 3, as
 * published by the Free Software Foundation.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#include "epuckDriver2_0.hpp"
#include <string>
#include <cstddef>

EpuckDriver2_0::EpuckDriver2_0(ConfigFile* cf, int section)
  :Driver(cf, section, true, PLAYER_MSGQUEUE_DEFAULT_MAXLEN)
  ,EXPECTED_EPUCK_SIDE_VERSION(300) // Version 3.0
{
  std::string strSerialPort(cf->ReadString(section, "port", "/dev/rfcomm0"));
  this->serialPort = new SerialPort(strSerialPort);

  //-------------------- POSITION2D
  if(cf->ReadDeviceAddr(&this->position2dAddr, section, "provides",
                        PLAYER_POSITION2D_CODE, -1, NULL) == 0)
  {
    if(this->AddInterface(this->position2dAddr) != 0)
    {
      this->SetError(-1);
      return;
    }
    this->epuckPosition2d.reset(new EpuckPosition2d(this->serialPort));
  }

  //-------------------- IR
  if(cf->ReadDeviceAddr(&this->irAddr, section, "provides",
                        PLAYER_IR_CODE, -1, NULL) == 0)
  {
    if(this->AddInterface(this->irAddr) != 0)
    {
      this->SetError(-1);
      return;
    }
    this->epuckIR.reset(new EpuckIR(this->serialPort));
  }

  //-------------------- CAMERA
  if(cf->ReadDeviceAddr(&this->cameraAddr, section, "provides",
                        PLAYER_CAMERA_CODE , -1, NULL) == 0)
  {
    if(this->AddInterface(this->cameraAddr) != 0)
    {
      this->SetError(-1);
      return;
    }

    int sensor_x1 = cf->ReadInt(section, "sensor_x1", 240);
    int sensor_y1 = cf->ReadInt(section, "sensor_y1", 160);
    int sensor_width = cf->ReadInt(section, "sensor_width", 160);
    int sensor_height = cf->ReadInt(section, "sensor_height", 160);
    int zoom_fact_width = cf->ReadInt(section, "zoom_fact_width", 4);
    int zoom_fact_height = cf->ReadInt(section, "zoom_fact_height", 4);
    EpuckCamera::ColorModes color_mode;
    std::string strColorMode(cf->ReadString(section,
                                            "color_mode",
                                            "GREY_SCALE_MODE"));

    if(strColorMode == "GREY_SCALE_MODE")
    {
      color_mode = EpuckCamera::GREY_SCALE_MODE;
    }
    else if(strColorMode == "RGB_565_MODE")
    {
      color_mode = EpuckCamera::RGB_565_MODE;
    }
    else if(strColorMode == "YUV_MODE")
    {
      color_mode = EpuckCamera::YUV_MODE;
    }
    else
    {
      PLAYER_WARN("Invalid camera color mode, using default grey scale mode.");
      color_mode = EpuckCamera::GREY_SCALE_MODE;
    }

    this->epuckCamera.reset(new EpuckCamera(this->serialPort,
                                            sensor_x1, sensor_y1,
                                            sensor_width, sensor_height,
                                            zoom_fact_width, zoom_fact_height,
                                            color_mode));
  }

  //-------------------- RING LEDS
  if(cf->ReadDeviceAddr(&this->opaqueRingLEDAddr, section, "provides",
                        PLAYER_OPAQUE_CODE, -1, "ring_leds") == 0)
  {
    if(this->AddInterface(this->opaqueRingLEDAddr) != 0)
    {
      this->SetError(-1);
      return;
    }

    if(this->epuckLEDs.get() == NULL)
      this->epuckLEDs.reset(new EpuckLEDs(this->serialPort));
  }

  //-------------------- FRONT LED
  if(cf->ReadDeviceAddr(&this->opaqueFrontLEDAddr, section, "provides",
                        PLAYER_OPAQUE_CODE, -1, "front_led") == 0)
  {
    if(this->AddInterface(this->opaqueFrontLEDAddr) != 0)
    {
      this->SetError(-1);
      return;
    }

    if(this->epuckLEDs.get() == NULL)
      this->epuckLEDs.reset(new EpuckLEDs(this->serialPort));
  }

  //-------------------- BODY LED
  if(cf->ReadDeviceAddr(&this->opaqueBodyLEDAddr, section, "provides",
                        PLAYER_OPAQUE_CODE, -1, "body_led") == 0)
  {
    if(this->AddInterface(this->opaqueBodyLEDAddr) != 0)
    {
      this->SetError(-1);
      return;
    }

    if(this->epuckLEDs.get() == NULL)
      this->epuckLEDs.reset(new EpuckLEDs(this->serialPort));
  }
}

EpuckDriver2_0::~EpuckDriver2_0()
{
  delete serialPort;
}

int
EpuckDriver2_0::Setup()
{
  if(this->serialPort->initialize() == -1)
  {
    PLAYER_ERROR1("%s",this->serialPort->getError().c_str());
    return -1;
  }

  // Request e-puck side program version
  this->serialPort->sendInt(0x01);
  if(this->serialPort->recvUnsigned() != this->EXPECTED_EPUCK_SIDE_VERSION)
  {
    PLAYER_ERROR("The e-puck side program version isn't the expected");
    return -1;
  }

  if(epuckCamera.get() != NULL)
  {
    try
    {
      this->epuckCamera->Initialize();
      std::string version = this->epuckCamera->GetCameraVersion();
      PLAYER_MSG1(1,"E-puck camera initialized. Camera Version: %s", version.c_str());
    }
    catch(std::exception &e)
    {
      PLAYER_ERROR1("%s", e.what());
      return -1;
    }
  }

  this->StartThread();
  return 0;
}

int
EpuckDriver2_0::Shutdown()
{
  this->StopThread();
  return 0;
}

int
EpuckDriver2_0::Subscribe(player_devaddr_t addr)
{
  if(addr.interf == PLAYER_POSITION2D_CODE)
  {
    this->epuckPosition2d->ResetOdometry();
  }

  return Driver::Subscribe(addr);
}

int
EpuckDriver2_0::Unsubscribe(player_devaddr_t addr)
{
  if(addr.interf == PLAYER_POSITION2D_CODE)
  {
    this->epuckPosition2d->StopMotors();
  }
  else if(addr.interf == PLAYER_OPAQUE_CODE)
  {
    this->epuckLEDs->ClearInternal();
  }

  return Driver::Unsubscribe(addr);
}


int
EpuckDriver2_0::ProcessMessage(MessageQueue* resp_queue,
                            player_msghdr* hdr, void* data)
{
  //-------------------- POSITION2D
  if(Message::MatchMessage(hdr, PLAYER_MSGTYPE_CMD,
                           PLAYER_POSITION2D_CMD_VEL,
                           this->position2dAddr))
  {
    player_position2d_cmd_vel_t position_cmd_vel =
      *(player_position2d_cmd_vel_t *)data;

    this->epuckPosition2d->SetVel(position_cmd_vel.vel.px,
                                  position_cmd_vel.vel.pa);

    if(position_cmd_vel.vel.py != 0)
    {
      PLAYER_WARN("Ignored invalid sideways volocity command");
    }

    return 0;

  }else if(Message::MatchMessage(hdr, PLAYER_MSGTYPE_CMD,
                           PLAYER_POSITION2D_CMD_CAR,
                           this->position2dAddr))
  {
    player_position2d_cmd_car_t position_cmd_car =
      *(player_position2d_cmd_car_t *)data;

    this->epuckPosition2d->SetVel(position_cmd_car.velocity,
                                  position_cmd_car.angle);

    return 0;

  }else if(Message::MatchMessage(hdr, PLAYER_MSGTYPE_REQ,
                                 PLAYER_POSITION2D_REQ_GET_GEOM,
                                 this->position2dAddr))
  {
    EpuckPosition2d::BodyGeometry epuckGeom = this->epuckPosition2d->GetGeometry();

    player_position2d_geom_t playerGeom;
    playerGeom.pose.px = 0;
    playerGeom.pose.py = 0;
    playerGeom.pose.pa = 0;
    playerGeom.size.sw = epuckGeom.width;
    playerGeom.size.sl = epuckGeom.height;

    this->Publish(this->position2dAddr,
                  resp_queue,
                  PLAYER_MSGTYPE_RESP_ACK,
                  PLAYER_POSITION2D_REQ_GET_GEOM,
                  (void*)&playerGeom,
                  sizeof(playerGeom),
                  NULL);

    return 0;

  }else if(Message::MatchMessage(hdr, PLAYER_MSGTYPE_REQ,
                                 PLAYER_POSITION2D_REQ_SET_ODOM,
                                 this->position2dAddr))
  {
    player_position2d_set_odom_req_t* set_odom_req =
      (player_position2d_set_odom_req_t*)data;

    EpuckInterface::Triple epuckOdom;
    epuckOdom.x     = set_odom_req->pose.px;
    epuckOdom.y     = set_odom_req->pose.py;
    epuckOdom.theta = set_odom_req->pose.pa;

    this->epuckPosition2d->SetOdometry(epuckOdom);
    this->Publish(this->position2dAddr, resp_queue,
                  PLAYER_MSGTYPE_RESP_ACK, PLAYER_POSITION2D_REQ_SET_ODOM);

    return 0;

  }else if(Message::MatchMessage(hdr, PLAYER_MSGTYPE_REQ,
                                 PLAYER_POSITION2D_REQ_RESET_ODOM,
                                 this->position2dAddr))
  {
    this->epuckPosition2d->ResetOdometry();
    this->Publish(this->position2dAddr, resp_queue,
                  PLAYER_MSGTYPE_RESP_ACK, PLAYER_POSITION2D_REQ_RESET_ODOM);

    return 0;

  }
  //-------------------- IR
  else if(Message::MatchMessage(hdr, PLAYER_MSGTYPE_REQ,
                                PLAYER_IR_POSE,
                                this->irAddr))
  {
    std::vector<EpuckInterface::Triple> epuckGeom = this->epuckIR->GetGeometry();

    player_ir_pose_t playerGeom;
    playerGeom.poses_count = epuckGeom.size();
    std::vector<EpuckInterface::Triple>::iterator it = epuckGeom.begin();
    for(int count = 0;
        it < epuckGeom.end();
        it++, count++)
    {
      playerGeom.poses[count].px = it->x;
      playerGeom.poses[count].py = it->y;
      playerGeom.poses[count].pa = it->theta;
    }

    this->Publish(this->irAddr,
                  resp_queue,
                  PLAYER_MSGTYPE_RESP_ACK,
                  PLAYER_IR_POSE,
                  (void*)&playerGeom,
                  sizeof(playerGeom),
                  NULL);

    return 0;

  }
  //-------------------- RING LED
  else if(Message::MatchMessage(hdr, PLAYER_MSGTYPE_CMD,
                                PLAYER_OPAQUE_CMD,
                                this->opaqueRingLEDAddr))
  {
    player_opaque_data_t* opaque_data =
      (player_opaque_data_t *)data;

    bool ringLED[EpuckLEDs::RING_LEDS_NUM];
    for(unsigned led = 0; led < opaque_data->data_count; ++led)
    {
      ringLED[led] = opaque_data->data[led];
    }
    this->epuckLEDs->SetRingLED(ringLED);

    return 0;
  }
  //-------------------- FRONT LED
  else if(Message::MatchMessage(hdr, PLAYER_MSGTYPE_CMD,
                                PLAYER_OPAQUE_CMD,
                                this->opaqueFrontLEDAddr))
  {
    player_opaque_data_t* opaque_data =
      (player_opaque_data_t *)data;

    this->epuckLEDs->SetFrontLED(opaque_data->data[0]);

    return 0;
  }
  //-------------------- BODY LED
  else if(Message::MatchMessage(hdr, PLAYER_MSGTYPE_CMD,
                                PLAYER_OPAQUE_CMD,
                                this->opaqueBodyLEDAddr))
  {
    player_opaque_data_t* opaque_data =
      (player_opaque_data_t *)data;

    this->epuckLEDs->SetBodyLED(opaque_data->data[0]);

    return 0;
  }

  else
  {
    PLAYER_ERROR("Epuck:: Unhandled message");
    return -1;
  }
}

void
EpuckDriver2_0::Main()
{
  player_position2d_data_t posData;
  EpuckPosition2d::DynamicConfiguration epuckOdometry;

  player_ir_data_t irData;
  EpuckIR::IRData epuckIRData;

  player_camera_data_t cameraData;

  // If there are a camera, initialize the cameraData struct
  if(this->epuckCamera.get() != NULL)
  {
    unsigned imageWidth, imageHeight;
    EpuckCamera::ColorModes colorMode;
    this->epuckCamera->GetCameraData(imageWidth, imageHeight, colorMode);

    cameraData.width  = imageWidth;
    cameraData.height = imageHeight;

    switch (colorMode)
    {
    case EpuckCamera::GREY_SCALE_MODE:
      cameraData.bpp = 8;
      cameraData.format = PLAYER_CAMERA_FORMAT_MONO8;
      break;
    case EpuckCamera::RGB_565_MODE:
      cameraData.bpp = 16;
      cameraData.format = PLAYER_CAMERA_FORMAT_RGB565;
      break;
    case EpuckCamera::YUV_MODE:
      cameraData.bpp = 16;
      cameraData.format = PLAYER_CAMERA_FORMAT_MONO16;
      break;
    }

    cameraData.fdiv        = 1;
    cameraData.compression = PLAYER_CAMERA_COMPRESS_RAW;
    cameraData.image_count = cameraData.width*cameraData.height*cameraData.bpp/8;
  }

  while(true)
  {
    pthread_testcancel();

    if(this->InQueue->Empty() == false)
    {
      ProcessMessages();
    }

    if(this->epuckPosition2d.get() != NULL)
    {
      epuckOdometry = this->epuckPosition2d->UpdateOdometry();
      posData.pos.px = epuckOdometry.pose.x;
      posData.pos.py = epuckOdometry.pose.y;
      posData.pos.pa = epuckOdometry.pose.theta;
      posData.vel.px = epuckOdometry.velocity.x;
      posData.vel.py = epuckOdometry.velocity.y;
      posData.vel.pa = epuckOdometry.velocity.theta;

      this->Publish(this->position2dAddr,NULL,
                    PLAYER_MSGTYPE_DATA, PLAYER_POSITION2D_DATA_STATE,
                    (void*)&posData,sizeof(posData), NULL);
    }

    if(this->epuckIR.get() != NULL)
    {
      epuckIRData = this->epuckIR->GetIRData();
      irData.voltages_count = epuckIRData.voltages.size();
      irData.ranges_count = epuckIRData.ranges.size();

      std::vector<float>::iterator itVoltages, itRanges;
      itVoltages = epuckIRData.voltages.begin();
      itRanges   = epuckIRData.ranges.begin();
      for(int count = 0;
          itVoltages < epuckIRData.voltages.end();
          itVoltages++, itRanges++, count++)
      {
        irData.voltages[count] = *itVoltages;
        irData.ranges[count] = *itRanges;
      }

      this->Publish(this->irAddr,NULL,
                    PLAYER_MSGTYPE_DATA, PLAYER_IR_DATA_RANGES,
                    (void*)&irData,sizeof(irData), NULL);
    }

    if(this->epuckCamera.get() != NULL)
    {
      this->epuckCamera->GetImage(cameraData.image);
      this->Publish(this->cameraAddr,NULL,
                    PLAYER_MSGTYPE_DATA, PLAYER_CAMERA_DATA_STATE,
                    (void*)&cameraData,sizeof(cameraData), NULL);
    }

  }
}

Driver*
EpuckDriver2_0::EpuckDriver2_0_Init(ConfigFile* cf, int section)
{
  return((Driver*)(new EpuckDriver2_0(cf, section)));
}

void
EpuckDriver2_0::EpuckDriver2_0_Register(DriverTable* table)
{
  table->AddDriver((char*)"epuck", EpuckDriver2_0_Init);
}

/*! \relates EpuckDriver2_0
 * Function called from player server for to register the e-Puck driver.
 */
extern "C"
{
  int player_driver_init(DriverTable* table)
  {
    PLAYER_MSG0(1, "Registering epuck driver.");
    EpuckDriver2_0::EpuckDriver2_0_Register(table);
    return (0);
  }
}
