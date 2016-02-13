def run_length_encoding(word):
    print word[0] + str(len(word) - 2) + word[-1]
    i = len(word)-3
    k = 0
    while i > 1:
        while k <= len(word)-2-i:
            print word[:k+1] + str(i) + word[i+k+1:]
            k += 1
        i -= 1

print run_length_encoding("nailed")

# void printAll(string st) {
#     cout << st[0] << st.size()-2 << st[st.size()-1] << endl;
#     for(int i=st.size()-3; i>=1; i--) {
#         for(int k=0; k<=st.size()-2-i; k++)
#             cout << st.substr(0,k+1) << i << st.substr(i+k+1) << endl;
#     }
#     cout << st << endl;
#  }