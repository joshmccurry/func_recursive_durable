# Durable Function Heap Creation

The contained function code creates a function app following the below psuedocode.

Psuedocode
```
queue := durable task framework 
for each item in queue                                  ( O(n^3 + n) )
    check orchestration
//Host Process loop, User code below
all := results from function
await for each toplevel 		                ( O(n) )
    queue += toplevel sub orchestration
    await for each level2                               ( O(n^2) )
        queue += level2 sub orchestration
        await for each level3				( O(n^3) ) 
            queue += level3 sub orchestration
            await activity
                queue += activity management
                worktask   := activity operation
                append all with worktask
```
---

The durable task framework will translate the orchestrations to queue processes via the taskhub.

However this representation forms a tree.

![Tree Data Structure](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Tree_%28computer_science%29.svg/300px-Tree_%28computer_science%29.svg.png)

[Tree Doc](https://en.wikipedia.org/wiki/Tree_(data_structure))

[Queue Doc](https://en.wikipedia.org/wiki/Queue_(abstract_data_type))

As the complexity increases the orchestrations become harder to manage from the queue causing the durable task framework to timeout.

This can be seen from the heap documentation below.

![Heap Datastructure](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Max-Heap-new.svg/300px-Max-Heap-new.svg.png)

[Heap Doc](https://en.wikipedia.org/wiki/Heap_(data_structure))
