/***************************************************************************************************************

Title:		UART1_RX_CHAR.s

Author:		Inspired Microchip library
			Bonani Michael

History:
	21/12/05	Start day
	12/03/07	added rx buffer

****************************************************************************************************************/
;to be used with uart_txrx_char.h

.include "e_epuck_ports.inc"
;.equiv	BAUDRATE, 115200 ;115000, 230400, 460800, 921600 
;.global _BAUDRATE
;_BAUDRATE: .space 4



.extern _U2RXRcvCnt
.extern _U2RXReadCnt
;.extern _cVariable

.section .text

;MY_BAUDRATE: .int 10

.global _e_init_uart2
_e_init_uart2:
		;.equiv BAUDRATE, W0
		; Init uart 2 at 11500bps, 8 data bits, 1 stop bit, Enable ISR for RX and TX
		; Initialize and Enable UART1 for Tx and Rx
		clr     U2MODE                              ; Set SFRs to a known state
		clr     U2STA
		bclr    U2STA, #URXISEL1
		bclr    U2STA, #URXISEL0

		bclr    IFS1, #U2RXIF
		bset    IEC1, #U2RXIE                       ; Enable Rx ISR processing

		bset    U2MODE, #UARTEN                     ; Enable UART
		;.set	_BAUDRATE, W0
		;.set	W0, _BAUDRATE
		;mov	W0, _BAUDRATE
		;mov	W0, W1
		;mov	W0, _cVariable;
		;BAUDRATE	= W0
		;mov     #(((FCY/BAUDRATE)/16)-1), W0        ; Initialize Baud rate
		;mov 	((FCY/W0)/16)-1, W0
		;.equiv	BAUDRATE, ((FCY/W0)/16)-1
		;mov	BAUDRATE, W0:W1
		;.equiv result, ((FCY/BAUDRATE)/16)-1
		;mov	FCY, W6
		;mov	W0, W7			; baudrate saved in W7
		;div.s	W6, W7;		; FCY/baudrate = W0, remainder W1
		
		;mov	result, W0
		;mov	#((FCY/16)-1), W0
		;div.ud	#FCY, W0
		mov     w0, U2BRG                           ; 9600 to 115200 Kbaud
		
		bclr    IFS1, #U2TXIF                      ; Enable Txmit ISR processing
		bset    IEC1, #U2TXIE

		; set a higher priority on UART interrupt ( so an ISR can use uart )
		; uart is slow, don't abuse it in interrupt
		bclr.b INTCON1+1,#7
		mov IPC6, w0
		mov #0xFF00, w1
		and w1,w0,w0
		mov #0x0055, w1
		add w1,w0,w0
		mov w0,IPC6

		bset    U2STA, #UTXISEL
		bset    U2STA, #UTXEN                       ; Enable Transmission
		
		; Reception counters to 0
		clr _U2RXRcvCnt
		clr _U2RXReadCnt
		return


.end


