class Twitter:
    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list) 
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
         self.count += 1
         self.tweetMap[userId].append([self.count, tweetId])
        

    def getNewsFeed(self, userId: int) -> List[int]:
        candidates = []
        people = self.followMap[userId] | {userId}
        for uid in people:
            candidates.extend(self.tweetMap[uid])
        candidates.sort(reverse=True)
        return [tweetId for _, tweetId in candidates[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
                self.followMap[followerId].add(followeeId)

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
                self.followMap[followerId].discard(followeeId)
