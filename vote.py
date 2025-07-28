    # <<<<<<<<<<< VOTING SYSTEM💥🙏>>>>>>>>>>>>>>>>>>>>>>>>>>>

class VotingSystem:
    def __init__(self, candidates):
        self.candidates = candidates
        self.votes = {name: 0 for name in candidates}

    def display_candidates(self):
        print("\nNominees on the Ballot :")
        for idx, name in enumerate(self.candidates, 1):
            print(f"{idx}. {name}")

    def cast_vote(self):
        self.display_candidates()
        try:
            choice = int(input("\nPick a number to vote for your chosen nominee : "))
            if 1 <= choice <= len(self.candidates):
                selected = self.candidates[choice - 1]
                self.votes[selected] += 1
                print(f"✅ Your vote has been officially cast **{selected}**!")
            else:
                print("❌ That’s not a valid option. Please pick again.")
        except ValueError:
            print("❌ Kindly provide a valid number.")

    def show_results(self):
        print("\n📊 Voting Results:")
        for candidate, count in self.votes.items():
            print(f"- {candidate}: {count} vote(s)")

    def show_winner(self):
        print("\n🏆 Election Outcome:")
        max_votes = max(self.votes.values())
        winners = [name for name, count in self.votes.items() if count == max_votes]

        if len(winners) == 1:
            print(f"The winner is 🎉 {winners[0]} with {max_votes} votes!")
        else:
            print("It's a tie between:")
            for winner in winners:
                print(f"🔹 {winner} ({max_votes} votes)")

    def run(self):
        while True:
            print("\n========== VoteWise Menu ==========")
            print("1. Vote")
            print("2. Show Results")
            print("3. Show Winner")
            print("4. Exit")
            choice = input("Select an option (1-4): ")

            match choice:
                case '1':
                    self.cast_vote()
                case '2':
                    self.show_results()
                case '3':
                    self.show_winner()
                case '4':
                    print("🔚 Exiting... Your vote has been received! 🏆")
                    break
                case _:
                    print("⚠️Invalid choice! Please select a number between 1️⃣ and 4️⃣")


if __name__ == "__main__":
    candidate_list = ["Sarthak", "Rudra", "Riya", "Riddhi"]
    system = VotingSystem(candidate_list)
    system.run()
