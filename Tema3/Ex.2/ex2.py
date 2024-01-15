class TriviaGame:
    def __init__(self):
        self.questions = [

            {
                "question": "Care este cel mai lung fluviu din lume?",
                "options": ["Nil", "Amazon", "Mississippi", "Yangtze"],
                "answer": "Amazon"
            },
            {
                "question": "Cine a pictat Mona Lisa?",
                "options": ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Michelangelo"],
                "answer": "Leonardo da Vinci"
            },
            {
                "question": "Câte continente există pe Pământ?",
                "options": ["4", "6", "7", "8"],
                "answer": "7"
            },
            {
                "question": "Care este cel mai înalt munte din lume?",
                "options": ["Mont Blanc", "Everest", "K2", "Kilimanjaro"],
                "answer": "Everest"
            },
            {
                "question": "Care este cel mai rapid animal terestru?",
                "options": ["Leopardul", "Ghepardul", "Leul", "Antilopa"],
                "answer": "Ghepardul"
            },
            {
                "question": "Cine a scris piesa de teatru „Romeo și Julieta”?",
                "options": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Fyodor Dostoevsky"],
                "answer": "William Shakespeare"
            },
            {
                "question": "Care este cel mai mare ocean al lumii?",
                "options": ["Oceanul Atlantic", "Oceanul Indian", "Oceanul Arctic", "Oceanul Pacific"],
                "answer": "Oceanul Pacific"
            },
            {
                "question": "Cine a inventat becul electric?",
                "options": ["Thomas Edison", "Nikola Tesla", "Galileo Galilei", "Albert Einstein"],
                "answer": "Thomas Edison"
            },
        ]
        self.score = 0
    def display_question(self, question):
        print(question["question"])
        for i, option in enumerate(question["options"], start=1):
            print(f"{i}. {option}")
        user_choice = input("Alegeți răspunsul (introduceți numărul corespunzător): ")
        return int(user_choice)

    def play(self):
        print("Bun venit în jocul de Trivia! Răspundeți la întrebări:")
        for question in self.questions:
            user_choice = self.display_question(question)
            if question["options"][user_choice - 1] == question["answer"]:
                print("Răspuns corect!")
                self.score += 1
            else:
                print(f"Răspuns greșit! Răspunsul corect era: {question['answer']}")

        print(f"Jocul s-a încheiat! Scorul dvs. este: {self.score} / {len(self.questions)}")
# Inițierea și pornirea jocului
if __name__ == "__main__":
    game = TriviaGame()
    game.play()
