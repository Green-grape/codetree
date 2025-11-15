n, m, q = map(int, input().split())


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


circles = []
for _ in range(m):
    nums = list(map(int, input().split()))
    k = nums[0]
    node_dict = {}
    for i in range(1, k + 1):
        if i == 1:
            root = Node(nums[i])
            curr = root
            node_dict[nums[i]] = root
        else:
            new_node = Node(nums[i])
            curr.right = new_node
            new_node.left = curr
            curr = new_node
            node_dict[nums[i]] = new_node
    root.left = curr
    curr.right = root
    circles.append(node_dict)


def get_node_by_val(val):
    for i, circle in enumerate(circles):
        if val in circle:
            return i, circle[val]
    return None


def merge_circles(x, y):
    circle_idx_x, node_x = get_node_by_val(x)
    circle_idx_y, node_y = get_node_by_val(y)
    if circle_idx_x == circle_idx_y:
        return

    # Connect the two circles
    left_x = node_x.left
    right_x = node_x.right
    left_y = node_y.left
    right_y = node_y.right

    node_x.right = node_y
    node_y.left = node_x
    if right_x:
        right_x.left = left_y
    if left_y:
        left_y.right = right_x

    circles[circle_idx_x].update(circles[circle_idx_y])
    del circles[circle_idx_y]


def divide_circle(x, y):
    circle_idx, node_x = get_node_by_val(x)
    _, node_y = get_node_by_val(y)
    if circle_idx is None or node_x is node_y:
        return

    circle = circles[circle_idx]

    new_circle = {}
    head = node_x
    curr = node_x
    while True:
        new_circle[curr.val] = curr
        next_node = curr.right
        circle.pop(curr.val)
        if next_node is node_y:
            break
        curr = next_node

    # Adjust pointers to split the circles
    head.left.right = node_y
    node_y.left.right = head
    node_y.left = head.left
    head.left = node_y.left

    circles.append(new_circle)
    circles[circle_idx] = circle


def print_circles():
    ret = []
    for circle in circles:
        head = circle[list(circle.keys())[0]]
        curr = circle[list(circle.keys())[0]]
        res = []
        while True:
            res.append(curr.val)
            curr = curr.right
            if curr is head:
                break
        ret.append("->".join(map(str, res)))
    print("\n".join(ret))


ret = []
for _ in range(q):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        _, x, y = cmd
        merge_circles(x, y)
    elif cmd[0] == 2:
        _, x, y = cmd
        divide_circle(x, y)
    else:
        _, x = cmd
        circle_idx, node_x = get_node_by_val(x)
        # get smallest value in the circle
        curr = node_x
        min_val = curr.val
        while True:
            curr = curr.right
            if curr.val < min_val:
                min_val = curr.val
            if curr is node_x:
                break
        circle_idx, node_x = get_node_by_val(min_val)
        curr = node_x
        res = []
        while True:
            res.append(str(curr.val))
            curr = curr.left
            if curr is node_x:
                break
        ret.append(" ".join(res))
print("\n".join(ret))


# 1 4 3
# 2 8 7 5 6
