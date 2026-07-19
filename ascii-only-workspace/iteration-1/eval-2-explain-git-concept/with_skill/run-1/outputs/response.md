```
#   # ##### ####   #### #####
## ## #     #   # #     #
# # # ####  ####  #  ## ####
#   # #     #  #  #   # #
#   # ##### #   #  #### #####

  before                      after
        A--B  feat                  A--B
       /                           /    \
  --o--C--D  main             --o--C--D--M   <- new merge commit
                                             [ history kept as-is ]

    #   #  ####
    #   # #
    #   #  ###
     # #      #
      #   ####

####  ##### ####   ###   #### #####
#   # #     #   # #   # #     #
####  ####  ####  #####  ###  ####
#  #  #     #   # #   #     # #
#   # ##### ####  #   # ####  #####

  before                      after
        A--B  feat                       A'--B'  feat
       /                                /
  --o--C--D  main             --o--C--D      <- linear
                                             [ copies A' B', new hashes ]

  +---------------------+----------------------+
  |        MERGE        |        REBASE        |
  +---------------------+----------------------+
  | keeps true history  | straight clean line  |
  | adds commit M       | rewrites commits     |
  | ok on shared branch | private branch only  |
  +---------------------+----------------------+

   shared / pushed branch --> MERGE
   local-only branch      --> REBASE ok
```
