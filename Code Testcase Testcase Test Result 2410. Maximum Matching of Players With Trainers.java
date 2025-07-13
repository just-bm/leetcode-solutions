class Solution {
    public int matchPlayersAndTrainers(int[] players, int[] trainers) {
        int total_players = players.length;
        int total_trainers = trainers.length;
        if (total_trainers <= 0){
            return -1;
        }
        int count = 0;
        Arrays.sort(players);
        Arrays.sort(trainers);
        int j = 0;
        int i = 0;
        while (i < total_players && j < total_trainers) {
            if (players[i] <= trainers[j]) {
                count++;
                i++;
                j++;
            }else{
                j++;
            }
        }
        return count;
    }
}
