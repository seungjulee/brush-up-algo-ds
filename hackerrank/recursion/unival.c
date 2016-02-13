static int count=0;
public static boolean findUni(BSTNode <Integer> node){
    if(node == null) return true;
    boolean left = findUni(node.left);
    boolean right =  findUni(node.right);
    if(left && right && (node.left==null || node.left.data == node.data) && 
            (node.right==null ||node.right.data == node.data)){
        count++;
        return true;
    }
    return false;
}