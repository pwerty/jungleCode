#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int elementCount, queryCount, targetValue;
vector<int> elements;

bool isPossible(int midIndex) {
	if (elements[midIndex] >= targetValue) return true;
	return false;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> elementCount >> queryCount;

	for (int i = 0; i < elementCount; i++) {
		int inputValue;
		cin >> inputValue;
		elements.push_back(inputValue);
	}

	sort(elements.begin(), elements.end());

	for (int i = 0; i < queryCount; i++) {
		cin >> targetValue;

		int left = 0, right = elements.size() - 1, resultIndex = -1;

		while (left <= right) {
			int midIndex = (left + right) / 2;

			if (isPossible(midIndex)) {
				if (elements[midIndex] == targetValue) resultIndex = midIndex;
				right = midIndex - 1;
			}
			else {
				left = midIndex + 1;
			}
		}
		cout << resultIndex << '\n';
	}
}