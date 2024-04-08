import java.util.PriorityQueue;
import java.util.Comparator;
import java.util.Arrays;

class Job implements Comparable<Job>{
    // 요청 시각, 소요 시간
    int requestT, requireT, startT;
    
    Job (int requestT, int requireT, int startT) {
        this.requestT = requestT; this.requireT= requireT; this.startT = startT;
    }

    
    @Override
    public int compareTo(Job other) {
        if (this.startT != other.startT) return -(this.startT - other.startT);
        return this.requireT - other.requireT;
    }
}

class Solution {
    public int solution(int[][] jobs) {
        int answer = 0;
        int jobLen = jobs.length;
        
        // 요청 시각 정렬 -> 같은 시각이면 소요 시간으로 정렬
        Arrays.sort(jobs, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if (o1[0]!=o2[0]) return o1[0]-o2[0];
                else return o1[1]-o2[1]; 
            }
        });
        
        int time = jobs[0][0];
        PriorityQueue<Job> pq = new PriorityQueue<>(); 
        for (int i=0; i< jobLen; i++) {
            int currR = jobs[i][0], currD = jobs[i][1]; // 요청 시각(기준), 소요 시간
            boolean flag = true;
            
            // 작업 대기열 업데이트 
            while (pq.size() > 0) {
                Job job = pq.remove();
                // 시작 시각 업데이트
                if (job.startT < 0) {
                    job.startT = Math.max(time, job.requestT);
                    time = job.startT;
                }
                
                if (job.startT + job.requireT <= currR) {
                    answer += time + job.requireT - job.requestT;

                    // 이전 작업 중이던 작업들을 끝냈을 시각이 현재 들어오는 작업 시각과 같다면 넣고 같이 생각해야
                    if (flag && time + job.requireT == currR) {
                        pq.add(new Job(currR, currD, -1));
                        flag = false;
                    }
                    
                    time += job.requireT;
                }
                else {
                    
                    pq.add(job); 
                    break;
                }
            }
            
            if (flag) pq.add(new Job(currR, currD, -1));

        }
        

        while (pq.size() > 0) {
            Job job = pq.remove();
            answer += time + job.requireT - job.requestT;
            time += job.requireT;
        }
        
        return answer/jobLen;
    }
}