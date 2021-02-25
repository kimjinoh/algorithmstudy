import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int target = sc.nextInt();
		int[] numbers = {1,1,1,1,1};
		class Solution {
			public int dfs(int prev, int index, int[] numbers, int target) {
				if (index >= numbers.length) {
					if (target == prev) {
						return 1;
					}
					return 0;
				}
				int cur1 = prev + numbers[index];
				int cur2 = prev - numbers[index];
				int ans = 0;
				ans += dfs(cur1, index + 1, numbers, target);
				ans += dfs(cur2, index + 1, numbers, target);
				return ans;
			}

			public int solution(int[] numbers, int target) {
				int current = numbers[0];
				int answer = 0;
				answer += dfs(current, 1, numbers, target);
				answer += dfs(-current, 1, numbers, target);
				System.out.println(answer);
				return answer;
			}
		}
		Solution sol = new Solution();
		sol.solution(numbers, target);
	}

}