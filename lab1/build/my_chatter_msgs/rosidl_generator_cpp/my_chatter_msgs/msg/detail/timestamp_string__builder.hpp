// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from my_chatter_msgs:msg/TimestampString.idl
// generated code does not contain a copyright notice

#ifndef MY_CHATTER_MSGS__MSG__DETAIL__TIMESTAMP_STRING__BUILDER_HPP_
#define MY_CHATTER_MSGS__MSG__DETAIL__TIMESTAMP_STRING__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "my_chatter_msgs/msg/detail/timestamp_string__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace my_chatter_msgs
{

namespace msg
{

namespace builder
{

class Init_TimestampString_time
{
public:
  explicit Init_TimestampString_time(::my_chatter_msgs::msg::TimestampString & msg)
  : msg_(msg)
  {}
  ::my_chatter_msgs::msg::TimestampString time(::my_chatter_msgs::msg::TimestampString::_time_type arg)
  {
    msg_.time = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_chatter_msgs::msg::TimestampString msg_;
};

class Init_TimestampString_input
{
public:
  Init_TimestampString_input()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TimestampString_time input(::my_chatter_msgs::msg::TimestampString::_input_type arg)
  {
    msg_.input = std::move(arg);
    return Init_TimestampString_time(msg_);
  }

private:
  ::my_chatter_msgs::msg::TimestampString msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_chatter_msgs::msg::TimestampString>()
{
  return my_chatter_msgs::msg::builder::Init_TimestampString_input();
}

}  // namespace my_chatter_msgs

#endif  // MY_CHATTER_MSGS__MSG__DETAIL__TIMESTAMP_STRING__BUILDER_HPP_
