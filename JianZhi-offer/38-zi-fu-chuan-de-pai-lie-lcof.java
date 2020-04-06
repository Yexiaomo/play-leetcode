class Solution {
    Set<String> rst = new HashSet<>();
    public String[] permutation(String s) {
        if(s == null || s.length() == 0)
            return new String[0];
        boolean[] visited = new boolean[s.length()];
        process(s, "", visited);
        return rst.toArray(new String[rst.size()]);
    }
    public void process(String s, String letter, boolean[] visited){
        if(s.length() == letter.length()){
            rst.add(letter);
            return;
        }
        for(int i = 0; i < s.length(); i++){
            char temp = s.charAt(i);
            if(visited[i])
                continue;
            visited[i] = true;
            process(s, letter+String.valueOf(temp), visited);
            visited[i] = false;
        }
    }
}
