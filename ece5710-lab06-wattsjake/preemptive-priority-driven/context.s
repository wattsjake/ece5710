 /****************************************************************************
 * SysTick_Handler
 * Interrupt Service Routine for system tick counter
 * The name of this function cannot be changed - it establishes the linkage
 *****************************************************************************/
    .syntax unified
    .text
    .thumb
    .thumb_func
    .align      4
    .globl      SysTick_Handler
    .type       SysTick_Handler, %function
SysTick_Handler:
    push   {r4-r11, lr}
    ldr    r6,=SystemTick  // r6 is address of SystemTick
    ldr    r7,[r6]         // r7 is current tick
    add    r7,r7,#1        // increment tick
    str    r7,[r6]         // save new tick
    //keep this below
    ldr    r4,=CurrentTask // r4 is address of current task
    ldr    r5,[r4]         // r5 is current task
    str    sp,[r5,#0]      // stack pointer is first thing in TCB
    bl     scheduler
    str    r0,[r4]         // save new CurrentTask
    ldr    sp,[r0,#0]      // get sp from new current task
    pop    {r4-r11, pc}

    .thumb_func
    .align      4
    .globl      SVC_Handler
    .type       SVC_Handler, %function
SVC_Handler:
    push   {r4-r11, lr}
    ldr    r4,=CurrentTask // r4 is address of current task
    ldr    r5,[r4]         // r5 is current task
    str    sp,[r5,#0]      // stack pointer is first thing in TCB
    bl     scheduler
    str    r0,[r4]         // save new CurrentTask
    ldr    sp,[r0,#0]      // get sp from new current task
    pop    {r4-r11, pc}

	.thumb_func
    .align      4
    .globl      Yield
    .type       Yield, %function
Yield:
	svc #0 // raise SVC interrupt
	bx lr  // return from subroutine

    .end
