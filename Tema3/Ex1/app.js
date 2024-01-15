import React, { useState, useEffect } from 'react';

const sounds = [
  { key: '1', sound: 'sound1.mp3' },
  { key: '2', sound: 'sound2.mp3' },
  { key: '3', sound: 'sound3.mp3' },
  { key: '4', sound: 'sound4.mp3' },
];

function App() {
  const [sequence, setSequence] = useState([]);
  const [userSequence, setUserSequence] = useState([]);
  const [step, setStep] = useState(0);
  const [gameOver, setGameOver] = useState(false);

  const startGame = () => {
    const newSequence = getNewSequence();
    setSequence(newSequence);
    setUserSequence([]);
    setStep(0);
    setGameOver(false);
  };

  const getNewSequence = () => {
    const newSequence = [];
    for (let i = 0; i < Math.floor(Math.random() * 10) + 5; i++) {
      newSequence.push(sounds[Math.floor(Math.random() * sounds.length)].key);
    }
    return newSequence;
  };

  const playSound = (key) => {
    const sound = sounds.find((s) => s.key === key);
    const audio = new Audio(sound.sound);
    audio.play()
      .then(() => {
        setUserSequence([...userSequence, key]);
      })
      .catch((error) => {
        console.error('Eroare la redarea sunetului:', error);
      });
  };

  useEffect(() => {
    if (userSequence.length === step) {
      if (userSequence.every((value, index) => value === sequence[index])) {
        if (step === sequence.length - 1) {
          alert('Ai câștigat!');
          startGame();
        } else {
          setStep((prevStep) => prevStep + 1);
        }
      } else {
        alert('Joc terminat!');
        setGameOver(true);
      }
    }
  }, [userSequence, sequence, step]);

  return (
    <div>
      <h1>Joc de Memorie Audio</h1>
      <button onClick={startGame}>Începe Jocul</button>

      {gameOver && <p>Joc Terminat!</p>}

      {sequence.map((key) => (
        <button key={key} onClick={() => playSound(key)}>
          {key}
        </button>
      ))}
    </div>
  );
}

export default App;