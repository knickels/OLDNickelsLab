/** This is an example of how to manage the e-puck LEDs in Player version 2.0.X
 */
#include <stdio.h>
#include <libplayerc/playerc.h>
#include <unistd.h>

int main(int argc, const char **argv)
{
  playerc_client_t *client;
  playerc_opaque_t *ringLEDs;
  playerc_opaque_t *frontLED;
  playerc_opaque_t *bodyLED;

  client = playerc_client_create(NULL, "localhost", 6665);
  if(playerc_client_connect(client) != 0)
  {
    fprintf(stderr, "error: %s\n", playerc_error_str());
    return -1;
  }
  ringLEDs = playerc_opaque_create(client, 0);
  if(playerc_opaque_subscribe(ringLEDs, PLAYERC_OPEN_MODE) != 0)
  {
    fprintf(stderr, "error: %s\n", playerc_error_str());
    return -1;
  }
  frontLED = playerc_opaque_create(client, 1);
  if(playerc_opaque_subscribe(frontLED, PLAYERC_OPEN_MODE) != 0)
  {
    fprintf(stderr, "error: %s\n", playerc_error_str());
    return -1;
  }
  bodyLED = playerc_opaque_create(client, 2);
  if(playerc_opaque_subscribe(bodyLED, PLAYERC_OPEN_MODE) != 0)
  {
    fprintf(stderr, "error: %s\n", playerc_error_str());
    return -1;
  }

  if(playerc_client_datamode(client, PLAYERC_DATAMODE_PULL) != 0)
  {
    fprintf(stderr, "error: %s\n", playerc_error_str());
    return -1;
  }
  if(playerc_client_set_replace_rule(client, -1, -1,
                                     PLAYER_MSGTYPE_DATA, -1, 1) != 0)
  {
    fprintf(stderr, "error: %s\n", playerc_error_str());
    return -1;
  }

  /* Turn on the ring LEDs 2 and 6, and the front and body LEDs. */
  player_opaque_data_t ringData, frontData, bodyData;
  ringData.data_count = 8;
  int led;
  for(led = 0; led < 8; led++)
  {
    ringData.data[led] = 0;
  }
  ringData.data[2] = 1;
  ringData.data[6] = 1;

  frontData.data_count = 1;
  frontData.data[0] = 1;

  bodyData.data_count = 1;
  bodyData.data[0] = 1;

  playerc_opaque_cmd(ringLEDs, &ringData);
  playerc_opaque_cmd(frontLED, &frontData);
  playerc_opaque_cmd(bodyLED, &bodyData);

  /* Without this sleep there will not be enough time for process all above  *
   * messages. If the camera interface is not in provides section of Player  *
   * configuration file, the time for e-puck initialization will be smaller, *
   * and consequently this sleep time will can be smaller.                   */
  usleep(3e6);

  /* Shutdown and tidy up */
  playerc_opaque_unsubscribe(ringLEDs);
  playerc_opaque_destroy(ringLEDs);
  playerc_opaque_unsubscribe(frontLED);
  playerc_opaque_destroy(frontLED);
  playerc_opaque_unsubscribe(bodyLED);
  playerc_opaque_destroy(bodyLED);
  playerc_client_disconnect(client);
  playerc_client_destroy(client);

  return 0;
}
