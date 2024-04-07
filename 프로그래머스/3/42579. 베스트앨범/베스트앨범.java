import java.util.HashMap;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

class Song {
    int genre = 0, play = 0, id = 0;
    
    Song (int genre, int play, int id) {
        this.genre = genre;
        this.play = play;
        this.id = id;
    }
    
    public int getGenre() {return this.genre;}
    public int getPlay() {return this.play;}
    public int getId() {return this.id;}
}

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        int musicLen = genres.length;
        ArrayList<Integer> answer = new ArrayList<>();
        HashMap<String, Integer> genreCount = new HashMap<>();
        ArrayList<Song> Songs = new ArrayList<>();
        
        for(int i=0; i<musicLen; i++) {
            genreCount.put(genres[i], genreCount.getOrDefault(genres[i], 0)+plays[i]);
        }
        
        for(int i=0; i<musicLen; i++) {
            Songs.add(new Song(genreCount.get(genres[i]), plays[i], i));
        }
        
        Comparator<Song> songComparator = Comparator.comparing(Song::getGenre, Comparator.reverseOrder())
                                                      .thenComparing(Song::getPlay, Comparator.reverseOrder())
                                                      .thenComparing(Song::getId);
        
        Collections.sort(Songs, songComparator);
        
        int prev = 0, count = 0;
        for(Song song: Songs) {
            if (prev == song.genre) {
                if (count < 2) {
                    answer.add(song.id);
                    count += 1;
                }
            }
            else {
                answer.add(song.id);
                prev = song.genre;
                count = 1;
            }
        }
        
        return answer.stream().mapToInt(i->i).toArray();
    }
}