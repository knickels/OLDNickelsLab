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

#include <p30f6014A.h>

#include <motor_led/e_epuck_ports.h>
#include <motor_led/e_init_port.h>
#include <motor_led/advance_one_timer/e_led.h>

#define LED_ON 1

void epuckPlayer();

int getselector()
{
  return SELECTOR0 + 2*SELECTOR1 + 4*SELECTOR2 + 8*SELECTOR3;
}

int main()
{
  /* Init System */
  e_init_port();

  /* Reset if Power on (some problem for few robots) */
  if (RCONbits.POR)
  {
    RCONbits.POR=0;
    RESET();
  }

  /* Facility the loading program task. In some programs, if it is running
   * at upload program instant the reset can fail. Within this infinite
   * while loop the failure don't occur. */
  if(getselector() == 0)
  {
    e_set_led(0, LED_ON);
    while(1);
  }

  epuckPlayer();

  while(1);
  return 0;
}
