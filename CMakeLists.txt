cmake_minimum_required(VERSION 3.0.2)
project(roscam_sensors)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages


if( CATKIN_DEVEL_PREFIX OR catkin_FOUND OR CATKIN_BUILD_BINARY_PACKAGE)
    set(COMPILING_WITH_CATKIN 1)

    message(STATUS "---------------------------------------------------------------------")
    message(STATUS "Roscam_sensors is being built using CATKIN. ROS plugins will be compiled")
    message(STATUS "---------------------------------------------------------------------")

    set(ROS_DEPENDENCIES
        rospy
        std_msgs        
        )

    find_package(catkin REQUIRED COMPONENTS 
        message_generation
        ${ROS_DEPENDENCIES} 
        )
    
    add_message_files(
        FILES
        DHT22.msg
        )
        
    generate_messages(
        DEPENDENCIES
        std_msgs
        )

    catkin_package(
        CATKIN_DEPENDS 
            message_runtime
            ${ROS_DEPENDENCIES}  
        )
        

endif()


set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_AUTOMOC ON)
SET(CMAKE_AUTOUIC ON)

if(NOT CMAKE_VERSION VERSION_LESS 3.1)
    set(CMAKE_CXX_STANDARD 14)
    set(CMAKE_CXX_STANDARD_REQUIRED ON)
else()
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++14")
endif()

if (NOT WIN32)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g -fno-omit-frame-pointer")
endif()


###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)


#############
## Install ##
#############


catkin_install_python(PROGRAMS
  src/main.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)


#############
## Testing ##
#############

