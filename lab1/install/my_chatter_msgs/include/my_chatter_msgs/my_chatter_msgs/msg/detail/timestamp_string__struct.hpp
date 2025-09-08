// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from my_chatter_msgs:msg/TimestampString.idl
// generated code does not contain a copyright notice

#ifndef MY_CHATTER_MSGS__MSG__DETAIL__TIMESTAMP_STRING__STRUCT_HPP_
#define MY_CHATTER_MSGS__MSG__DETAIL__TIMESTAMP_STRING__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__my_chatter_msgs__msg__TimestampString __attribute__((deprecated))
#else
# define DEPRECATED__my_chatter_msgs__msg__TimestampString __declspec(deprecated)
#endif

namespace my_chatter_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct TimestampString_
{
  using Type = TimestampString_<ContainerAllocator>;

  explicit TimestampString_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->input = "";
      this->time = 0ll;
    }
  }

  explicit TimestampString_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : input(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->input = "";
      this->time = 0ll;
    }
  }

  // field types and members
  using _input_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _input_type input;
  using _time_type =
    int64_t;
  _time_type time;

  // setters for named parameter idiom
  Type & set__input(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->input = _arg;
    return *this;
  }
  Type & set__time(
    const int64_t & _arg)
  {
    this->time = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    my_chatter_msgs::msg::TimestampString_<ContainerAllocator> *;
  using ConstRawPtr =
    const my_chatter_msgs::msg::TimestampString_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<my_chatter_msgs::msg::TimestampString_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<my_chatter_msgs::msg::TimestampString_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      my_chatter_msgs::msg::TimestampString_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<my_chatter_msgs::msg::TimestampString_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      my_chatter_msgs::msg::TimestampString_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<my_chatter_msgs::msg::TimestampString_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<my_chatter_msgs::msg::TimestampString_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<my_chatter_msgs::msg::TimestampString_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__my_chatter_msgs__msg__TimestampString
    std::shared_ptr<my_chatter_msgs::msg::TimestampString_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__my_chatter_msgs__msg__TimestampString
    std::shared_ptr<my_chatter_msgs::msg::TimestampString_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TimestampString_ & other) const
  {
    if (this->input != other.input) {
      return false;
    }
    if (this->time != other.time) {
      return false;
    }
    return true;
  }
  bool operator!=(const TimestampString_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TimestampString_

// alias to use template instance with default allocator
using TimestampString =
  my_chatter_msgs::msg::TimestampString_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace my_chatter_msgs

#endif  // MY_CHATTER_MSGS__MSG__DETAIL__TIMESTAMP_STRING__STRUCT_HPP_
