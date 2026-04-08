import { useState } from "react";

function App() {
  const [text, setText] = useState("");
  const [targetLang, setTargetLang] = useState("en");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const handleTranslate = async () => {
    if (!text) return;

    setLoading(true);

    try {
      const response = await fetch("http://127.0.0.1:8000/translate", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          text: text,
          target_lang: targetLang,
        }),
      });

      const data = await response.json();
      console.log(data);
      setResult(data.translation);
    } catch (error) {
      console.error(error);
      setResult("Error during translation");
    }

    setLoading(false);
  };

  return (
    <div style={{ padding: "2rem", maxWidth: "600px", margin: "auto" }}>
      <h1>AI Translator</h1>

      <textarea
        rows={5}
        placeholder="Enter text..."
        value={text}
        onChange={(e) => setText(e.target.value)}
        style={{ width: "100%", marginBottom: "1rem" }}
      />

      <select
        value={targetLang}
        onChange={(e) => setTargetLang(e.target.value)}
      >
        <option value="en">English</option>
        <option value="fr">French</option>
        <option value="es">Spanish</option>
        <option value="de">German</option>
      </select>

      <br />
      <br />

      <button onClick={handleTranslate}>
        {loading ? "Translating..." : "Translate"}
      </button>

      <h3>Result:</h3>
      <p>{result}</p>
    </div>
  );
}

export default App;
