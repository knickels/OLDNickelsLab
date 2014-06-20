#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ(2.61)
AC_INIT([libepuck], [0.4.0], [fgar.renato@gmail.com])
AM_INIT_AUTOMAKE([-Wall -Werror foreign])
AM_PROG_LIBTOOL
AC_PROG_INSTALL

AC_CONFIG_SRCDIR([src/epuckInterface.cpp])
AC_CONFIG_HEADER([config.h])

dnl ========================================================================
dnl === Checks for programs.
dnl ========================================================================

AC_PROG_CXX

dnl ========================================================================
dnl === Checks for libraries.
dnl ========================================================================

PKG_CHECK_MODULES(PLAYERCORE_2_0, playercore >= 2.0 playercore < 2.1,
                  [AC_DEFINE([P_20],[1],[onFly])] [player_2_0=true],
                  [player_2_0=false])
AC_SUBST(PLAYERCORE_2_0_CFLAGS)
AM_CONDITIONAL([PLAYER_2_0], [test $player_2_0 = true])

PKG_CHECK_MODULES(PLAYERCORE_2_1, playercore >= 2.1 playercore < 2.2,
                  [AC_DEFINE([P_21],[1],[onFly])] [player_2_1=true],
                  [player_2_1=false])
AC_SUBST(PLAYERCORE_2_1_CFLAGS)
AM_CONDITIONAL([PLAYER_2_1], [test $player_2_1 = true])


dnl ========================================================================
dnl === Checks for typedefs, structures, and compiler characteristics.     =
dnl ========================================================================

AC_C_CONST

dnl ========================================================================
dnl === Checks for library functions.
dnl ========================================================================

AC_CONFIG_FILES([Makefile
                 src/Makefile
                 doc/doxygen/Makefile])
AC_OUTPUT
