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

#include <uart/e_uart_char.h>
#include <motor_led/e_epuck_ports.h>
#include <motor_led/e_init_port.h>
#include <motor_led/advance_one_timer/e_led.h>
#include <motor_led/advance_one_timer/e_motors.h>
#include <motor_led/advance_one_timer/e_agenda.h>
#include <a_d/e_prox.h>
#include <camera/fast_2_timer/e_poxxxx.h>

#define SIZEOF_CHAR 1
#define RING_LED_NUMBER 8
#define LED_ON 1
#define LED_OFF 0

unsigned char G_camera_buffer[6500] __attribute__ ((far));
unsigned int G_image_bytes_size = 0;

char recv_char()
{
  char message;

  while(!e_ischar_uart1()){} /* Wait until arrive a message */
  while(e_getchar_uart1(&message)==0);

  return message;
}

int ve_recv_int()
{
  char message[2];

  while(!e_ischar_uart1()){} /* Wait until arrive a message */
  while(e_getchar_uart1(message)==0);

  while(!e_ischar_uart1()){} /* Wait until arrive a message */
  while(e_getchar_uart1(message + 1)==0);

  int m0 = message[0];
  int m1 = message[1];

  return (m1<<8) | (m0 & 0xFF);
}

void ve_send_int(int integer)
{
  char message[2];
  message[0] = integer & 0x00FF;
  message[1] = (integer & 0xFF00) >> 8;

  e_send_uart1_char(message, SIZEOF_CHAR);
  while( e_uart1_sending() ){}
  e_send_uart1_char(message+1, SIZEOF_CHAR);
  while( e_uart1_sending() ){}
}

void send_char(char character)
{
  e_send_uart1_char(&character, SIZEOF_CHAR);
  while(e_uart1_sending());
}

void recv_vel()
{
  int stepsR,stepsL;

  stepsR = ve_recv_int();
  stepsL = ve_recv_int();

  if((stepsR > 1000)||(stepsR < -1000)||(stepsL > 1000)||(stepsL < -1000))
  {
    send_char(1);/* It signalize the end of operation. */
    return;
  }

  e_set_speed_right(stepsR);
  e_set_speed_left(stepsL);

  send_char(1);/* It signalize the end of operation. */
}

void send_steps()
{
  int steps_right,steps_left;

  steps_right = e_get_steps_right();
  steps_left = e_get_steps_left();
  e_set_steps_right(0);
  e_set_steps_left(0);

  ve_send_int(steps_right);
  ve_send_int(steps_left);
}

/** Stop the motor activities
 *
 * Set the speed for zero and clean the step counter
 */
void stop_motors()
{
  e_set_speed_right(0);
  e_set_speed_left(0);

  e_set_steps_right(0);
  e_set_steps_left(0);

  send_char(1);/* It signalize the end of operation. */
}

void read_ir_sensors()
{
  int ir_readings[8];
  int i;
  for(i=0; i<8; i++)
  {
    ir_readings[i] = e_get_prox(i);
  }

  for(i=0; i<8; i++)
  {
    ve_send_int(ir_readings[i]);
  }
}

void read_camera()
{
  e_poxxxx_launch_capture((char *)G_camera_buffer);

  while(!e_poxxxx_is_img_ready());

  e_send_uart1_char((char *)G_camera_buffer, G_image_bytes_size);
  while(e_uart1_sending());
}

void set_LEDs()
{
  char ring, body_front;
  ring = recv_char();
  body_front = recv_char();

  /* Each one of eight bits of "char ring" represents one of eight ring    *
   * LEDs in e-puck, the rightmost bit meaning the LED 0. With a bit being *
   * true the LED will be on, with a bit being false the LED will be off.  */
  int led;
  for(led = 0; led< RING_LED_NUMBER; led++)
  {
    if((ring&(0x01<<led))!=0)
    {
      e_set_led(led, LED_ON);
    }
    else
    {
      e_set_led(led, LED_OFF);
    }
  }

  if((body_front & 0x01) != 0)
  {
    e_set_front_led(LED_ON);
  }
  else
  {
    e_set_front_led(LED_OFF);
  }

  if((body_front & 0x02) != 0)
  {
    e_set_body_led(LED_ON);
  }
  else
  {
    e_set_body_led(LED_OFF);
  }

  send_char(1);/* Send a char to signalize the end set LED operation. */
}

/** Send the version of this program to driver.
 *
 * The sent value is a integer, being the two first digits reserved for
 * minor version, e.g. for version 1.02 would be sent the integer 102.
 */
void sendVersion()
{
  /* Version 3.0 */
  ve_send_int(300);
}

/** Get the version of camera in e-puck
 *
 * This function must be called after the camera to be initialized by
 * e_poxxxx_init_cam()
 * @return The camera version
 */
int getCameraVersion()
{
  const int device_id = 0xDC;

  int camera_version;
  unsigned char reg0, reg1;

  /* read the camera version */
  reg0 = e_i2cp_read(device_id, 0x0);
  reg1 = e_i2cp_read(device_id, 0x1);
  camera_version = reg0 << 8 | reg1;

  return camera_version;
}

void config_camera()
{
  e_poxxxx_init_cam();

  ve_send_int( getCameraVersion() );

  unsigned sensor_x1 = ve_recv_int();
  unsigned sensor_y1 = ve_recv_int();
  unsigned sensor_width = ve_recv_int();
  unsigned sensor_height = ve_recv_int();
  unsigned zoom_fact_width = ve_recv_int();
  unsigned zoom_fact_height = ve_recv_int();

  int color_mode = ve_recv_int();

  e_poxxxx_config_cam(sensor_x1,
                      sensor_y1,
                      sensor_width,
                      sensor_height,
                      zoom_fact_width,
                      zoom_fact_height,
                      color_mode);
  e_poxxxx_set_mirror(1,1);
  e_poxxxx_write_cam_registers();

  unsigned bytes_per_pixel;
  if(color_mode == GREY_SCALE_MODE)
  {
    bytes_per_pixel = 1;
  }
  else
  {
    bytes_per_pixel = 2;
  }

  G_image_bytes_size = (sensor_width/zoom_fact_width) * (sensor_height/zoom_fact_height) * bytes_per_pixel;

  send_char(1);/* It signalize the end of operation. */
}

void epuckPlayer()
{
  e_start_agendas_processing();
  e_init_motors();
  e_init_prox();
  e_init_uart1();

  /* Must send anything here or it don't work. Is it a bug? */
  e_send_uart1_char("epuckSide_v3.0", 14);

  unsigned a,b;

  /* Flash the LED's in a singular manner for show that this program is in
   * epuck memory */
  for(a=0; a<8; a++)
    for(b=0; b<20000; b++)
      e_set_led(a ,1); /* LED ON */

  for(a=0; a<8; a++)
    for(b=0; b<20000; b++)
      e_set_led(a ,0); /* LED OFF */

  char command;
  while(1)
  {
    command = recv_char();

    switch(command)
    {
    case 0x13:
      recv_vel();
      break;
    case 0x14:
      send_steps();
      break;
    case 0x16:
      read_ir_sensors();
      break;
    case 0x15:
      stop_motors();
      break;
    case 0x17:
      read_camera();
      break;
    case 0x18:
      set_LEDs();
      break;
    case 0x01:
      sendVersion();
      break;
    case 0x02:
      config_camera();
      break;
    }
  }
}
