# Check the compiler in use

IF (PLAYER_OS_WIN)
    IF (MINGW)
        SET (PLAYER_COMP_MINGW TRUE BOOL INTERNAL)
        MESSAGE (STATUS "Compiler is MinGW")
    ELSEIF (MSYS)
        SET (PLAYER_COMP_MSYS TRUE BOOL INTERNAL)
        MESSAGE (STATUS "Compiler is MSYS")
    ELSEIF (CYGWIN)
        SET (PLAYER_COMP_CYGWIN TRUE BOOL INTERNAL)
        MESSAGE (STATUS "Compiler is CygWin")
    ELSEIF (BORLAND)
        SET (PLAYER_COMP_BORLAND TRUE BOOL INTERNAL)
        MESSAGE (STATUS "Compiler is Borland")
    ELSEIF (MSVC or MSVC_IDE or MSVC60 or MSVC70 or MSVC71 or MSVC80 or CMAKE_COMPILER_2005)
        SET (PLAYER_COMP_MSVC TRUE BOOL INTERNAL)
        MESSAGE (STATUS "Compiler is Microsoft Visual Studio")
    ENDIF (MINGW)
ELSEIF (CMAKE_COMPILER_IS_GNUCC)
    SET (PLAYER_COMP_GNUCC TRUE BOOL INTERNAL)
    SET (PLAYER_COMP_GNU TRUE BOOL INTERNAL)
    MESSAGE (STATUS "Compiler is GNU gcc")
ELSEIF (CMAKE_COMPILER_IS_GNUCXX)
    SET (PLAYER_COMP_GNUCXX TRUE BOOL INTERNAL)
    SET (PLAYER_COMP_GNU TRUE BOOL INTERNAL)
    MESSAGE (STATUS "Compiler is GNU g++")
ENDIF (PLAYER_OS_WIN)