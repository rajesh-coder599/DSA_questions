# 32. Longest Valid Parentheses



# def longestValidParentheses(s):
#     prevln=0
#     mxln=0
#     currln=0
#     st=[]
#     for i in s:
#         if i==")":
#             if len(st)==0:
#                 mxln=max(mxln,currln+prevln)
#                 currln=0
#                 prevln=0
#             else:
#                 st.pop()
#                 currln+=2
#         else:
#             if len(st)==0:
#                 prevln+=currln
#                 mxln=max(mxln,prevln)
#                 currln=0
#             st.append(i)
#     if len(st)==0:
#         mxln=max(mxln,prevln+currln)
#     return mxln
a=[-1]
if not a:
    print(3)