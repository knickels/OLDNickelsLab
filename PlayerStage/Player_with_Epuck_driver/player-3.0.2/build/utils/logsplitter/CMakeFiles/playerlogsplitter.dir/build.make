# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# The program to use to edit the cache.
CMAKE_EDIT_COMMAND = /usr/bin/ccmake

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /usr/local/src/player-3.0.2

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /usr/local/src/player-3.0.2/build

# Include any dependencies generated for this target.
include utils/logsplitter/CMakeFiles/playerlogsplitter.dir/depend.make

# Include the progress variables for this target.
include utils/logsplitter/CMakeFiles/playerlogsplitter.dir/progress.make

# Include the compile flags for this target's objects.
include utils/logsplitter/CMakeFiles/playerlogsplitter.dir/flags.make

utils/logsplitter/CMakeFiles/playerlogsplitter.dir/logsplitter.o: utils/logsplitter/CMakeFiles/playerlogsplitter.dir/flags.make
utils/logsplitter/CMakeFiles/playerlogsplitter.dir/logsplitter.o: ../utils/logsplitter/logsplitter.c
	$(CMAKE_COMMAND) -E cmake_progress_report /usr/local/src/player-3.0.2/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building C object utils/logsplitter/CMakeFiles/playerlogsplitter.dir/logsplitter.o"
	cd /usr/local/src/player-3.0.2/build/utils/logsplitter && /usr/bin/gcc  $(C_DEFINES) $(C_FLAGS) -o CMakeFiles/playerlogsplitter.dir/logsplitter.o   -c /usr/local/src/player-3.0.2/utils/logsplitter/logsplitter.c

utils/logsplitter/CMakeFiles/playerlogsplitter.dir/logsplitter.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/playerlogsplitter.dir/logsplitter.i"
	cd /usr/local/src/player-3.0.2/build/utils/logsplitter && /usr/bin/gcc  $(C_DEFINES) $(C_FLAGS) -E /usr/local/src/player-3.0.2/utils/logsplitter/logsplitter.c > CMakeFiles/playerlogsplitter.dir/logsplitter.i

utils/logsplitter/CMakeFiles/playerlogsplitter.dir/logsplitter.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/playerlogsplitter.dir/logsplitter.s"
	cd /usr/local/src/player-3.0.2/build/utils/logsplitter && /usr/bin/gcc  $(C_DEFINES) $(C_FLAGS) -S /usr/local/src/player-3.0.2/utils/logsplitter/logsplitter.c -o CMakeFiles/playerlogsplitter.dir/logsplitter.s

utils/logsplitter/CMakeFiles/playerlogsplitter.dir/logsplitter.o.requires:
.PHONY : utils/logsplitter/CMakeFiles/playerlogsplitter.dir/logsplitter.o.requires

utils/logsplitter/CMakeFiles/playerlogsplitter.dir/logsplitter.o.provides: utils/logsplitter/CMakeFiles/playerlogsplitter.dir/logsplitter.o.requires
	$(MAKE) -f utils/logsplitter/CMakeFiles/playerlogsplitter.dir/build.make utils/logsplitter/CMakeFiles/playerlogsplitter.dir/logsplitter.o.provides.build
.PHONY : utils/logsplitter/CMakeFiles/playerlogsplitter.dir/logsplitter.o.provides

utils/logsplitter/CMakeFiles/playerlogsplitter.dir/logsplitter.o.provides.build: utils/logsplitter/CMakeFiles/playerlogsplitter.dir/logsplitter.o

# Object files for target playerlogsplitter
playerlogsplitter_OBJECTS = \
"CMakeFiles/playerlogsplitter.dir/logsplitter.o"

# External object files for target playerlogsplitter
playerlogsplitter_EXTERNAL_OBJECTS =

utils/logsplitter/playerlogsplitter: utils/logsplitter/CMakeFiles/playerlogsplitter.dir/logsplitter.o
utils/logsplitter/playerlogsplitter: utils/logsplitter/CMakeFiles/playerlogsplitter.dir/build.make
utils/logsplitter/playerlogsplitter: utils/logsplitter/CMakeFiles/playerlogsplitter.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking C executable playerlogsplitter"
	cd /usr/local/src/player-3.0.2/build/utils/logsplitter && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/playerlogsplitter.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
utils/logsplitter/CMakeFiles/playerlogsplitter.dir/build: utils/logsplitter/playerlogsplitter
.PHONY : utils/logsplitter/CMakeFiles/playerlogsplitter.dir/build

utils/logsplitter/CMakeFiles/playerlogsplitter.dir/requires: utils/logsplitter/CMakeFiles/playerlogsplitter.dir/logsplitter.o.requires
.PHONY : utils/logsplitter/CMakeFiles/playerlogsplitter.dir/requires

utils/logsplitter/CMakeFiles/playerlogsplitter.dir/clean:
	cd /usr/local/src/player-3.0.2/build/utils/logsplitter && $(CMAKE_COMMAND) -P CMakeFiles/playerlogsplitter.dir/cmake_clean.cmake
.PHONY : utils/logsplitter/CMakeFiles/playerlogsplitter.dir/clean

utils/logsplitter/CMakeFiles/playerlogsplitter.dir/depend:
	cd /usr/local/src/player-3.0.2/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /usr/local/src/player-3.0.2 /usr/local/src/player-3.0.2/utils/logsplitter /usr/local/src/player-3.0.2/build /usr/local/src/player-3.0.2/build/utils/logsplitter /usr/local/src/player-3.0.2/build/utils/logsplitter/CMakeFiles/playerlogsplitter.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : utils/logsplitter/CMakeFiles/playerlogsplitter.dir/depend

