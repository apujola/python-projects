import random
import time
import tkinter as tk

#/******************************************************************************************************
#The code creates a simple Typing Speed Test using Tkinter. It generates random words from a list and 
# the user types them into an Entry widget. The code tracks the user's accuracy and speed (in words per minute) 
# and displays the results in a Label widget. The user can start a new test by clicking the Start button
# and can reset the test by clicking the Reset button.
#******************************************************************************************************/

class TypingTest(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew']
        self.current_word = ''
        self.start_time = None
        self.total_time = 0
        self.num_words = 0
        self.num_correct = 0

        self.word_label = tk.Label(self, text=self.current_word, font=('Arial', 24))
        self.word_label.pack(pady=20)

        self.entry_var = tk.StringVar()
        self.entry_var.trace('w', self.check_word)
        self.entry = tk.Entry(self, textvariable=self.entry_var, font=('Arial', 24))
        self.entry.pack(pady=20)
        self.entry.focus()

        self.result_label = tk.Label(self, text='', font=('Arial', 16))
        self.result_label.pack(pady=20)

        self.pack()

    def start(self):
        self.new_word()
        self.start_time = time.time()

    def new_word(self):
        self.current_word = random.choice(self.words)
        self.word_label.config(text=self.current_word)
        self.entry_var.set('')

    def check_word(self, *args):
        if self.entry_var.get() == self.current_word:
            self.num_words += 1
            self.num_correct += 1
            self.total_time += time.time() - self.start_time
            self.result_label.config(text=f'Accuracy: {self.num_correct/self.num_words:.2%}, ' \
                f'Speed: {self.num_words/self.total_time*60:.2f} WPM')
            self.new_word()
            self.start_time = time.time()

    def reset(self):
        self.current_word = ''
        self.total_time = 0
        self.num_words = 0
        self.num_correct = 0
        self.word_label.config(text=self.current_word)
        self.entry_var.set('')
        self.result_label.config(text='')
        self.entry.focus()


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Typing Speed Test')

    app = TypingTest(root)

    start_button = tk.Button(root, text='Start', command=app.start)
    start_button.pack(side='left', padx=20, pady=20)

    reset_button = tk.Button(root, text='Reset', command=app.reset)
    reset_button.pack(side='right', padx=20, pady=20)

    root.mainloop()
