# 关于python中经常使用的链表操作

## 链表节点定义

```
class ListNode:
  def __init__(self,val=0,next=None):
    self.val = val
    self.next = next
```

## 基本操作

### 1. 遍历列表

```
  def traverse(head):
      current = head
      while current:
          print(current.val)
          current = current.next
```

### 2. 插入节点

1. 头部插入

```
def insert_head(head,val):
    new_node = ListNode(val)
    new_node.next = head
    return new_node
```

2. 尾部插入

```
def insert_at_tail(head,val):
  new_node = ListNode(val)
  if not head:
      return new_node
  current = head
  while current.next:
      #遍历一直找到最后的一个节点
      current = current.next
  current.next = new_node
  return head
```
3. 制定位置插入

```
def insert_at_position(head,val,position):
  if position == 0:
    return insert_at_head(head,val)
  current = head
  for i in range(position-1):
      if not current:
          return head
      current = current.next
  if current:
      new_node = ListNode(val)
      new_node.next = current.next
      current.next = new_node
  return head
```
### 3. 删除节点
1. 删除头节点

```
def delete_head(head):
  if not head:
    return Node
  return head.next
```
2. 删除尾节点

```
def delete_tail(head):
  if not head or not head.next:
      return None
  current = head
  #用来确定下个节点和下下个节点是否存在
  while current.next and current.next.next:
      current = current.next
  current.next = None
  return head
```
3. 删除指定值的节点

```
def delete_value(head,val):
  if not head:
      return None
  if head.val == val:
      return head.next
  current = head
  while current.next and current.next.val != val:
      current = current.next
  if current.next:
      current.next = current.next.next
  return head       
```
### 4. 查找节点

```
def find(head,val):
  current = head
  while current:
      if current.val == val:
          return current
      current = current.next
  return None
```
### 5. 获取列表长度
```
def get_length(head):
  if not head:
      return 0
  count = 0
  current = head
  while current:
      count +=1
      current = current.next
  return count
```
### 6. 反转列表
```
def reverse(head):
  prev = None
  current = head
  while current:
      # 1. 保存当前节点的下一个，防止因为指针更改丢失
      next_tmp = current.next
      # 2. 更改当前的指针为上一个节点
      current.next = prev
      # 3. 将当前节点定义为新的prev & 将‘下一个节点’改为当前节点
      prev = current
      current = next_tmp
  return prev
```
### 7. 循环检测

```
def has_cycle(head):
    if not head or not head.next:
        return False
    slow = head
    fast = head
    while fast and fast.next:
          slow  = slow.next
          fast = fast.next.next
          if slow == fast:
              return True
    return False
```
### 8. 寻找中间节点
```
def find_middle(head):
    if not head:
        return None
    slow = head
    fast = head
    while fast and fast.next:
          slow = slow.next
          fast = fast.next.next
    return slow
```
