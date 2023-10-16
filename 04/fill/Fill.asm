// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

// white or black flag 
@flag
M=0
(LOOP1)
    // store the number of remaining pixels
    @8192
    D=A
    @rem
    M=D
    // store the screen RAM address
    @SCREEN
    D=A-1
    @addr
    M=D
    // listens the keyboard input
    @KBD
    D=M
    // if input == 0, clears the screen
    @CLEAR
    D;JEQ
    // if input > 0, blackens the screen
    @BLACKEN
    D;JGT
    (BLACKEN)
        // if the screen is already black, go to END
        @flag
        D=M
        @END
        D;JGT
        // convert the flag
        @flag
        M=1
        // set the color black
        @color
        M=-1
        // go to LOOP2
        @LOOP2
        0;JMP
    (CLEAR)
        // if the screen is already clear, go to END
        @flag
        D=M
        @END
        D;JEQ
        // convert the flag
        @flag
        M=0
        // set the color white
        @color
        M=0
    (LOOP2)
        // get remaining black/white screen number
        @rem
        MD=M-1
        // if D < 0, go to END
        @END
        D;JLT
        // blacken/clear the next screen RAM
        @color
        D=M
        @addr
        AM=M+1
        M=D
        // go to LOOP2
        @LOOP2
        0;JMP
    (END)
    @LOOP1
    0;JMP
    