import { useState } from "react";

function App() {
  const [text, setText] = useState("");
  const [targetLang, setTargetLang] = useState("fr");
  const [result, setResult] = useState("");
  const [detectedLang, setDetectedLang] = useState("");
  const [loading, setLoading] = useState(false);

  const handleTranslate = async () => {
    if (!text.trim()) return;

    setLoading(true);

    try {
      const res = await fetch("http://127.0.0.1:8000/translate", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          text,
          target_lang: targetLang,
        }),
      });

      const data = await res.json();

      if (res.ok) {
        setResult(data.translation);
        setDetectedLang(data.source_language);
      } else {
        setResult(data.detail || "Error");
      }
    } catch (err) {
      setResult("Server error");
    }

    setLoading(false);
  };

  const handleClear = () => {
    setText("");
    setResult("");
    setDetectedLang("");
  };

  const handleCopy = () => {
    navigator.clipboard.writeText(result);
  };

  return (
    <div style={{ padding: "2rem", fontFamily: "Arial" }}>
      <h1 style={{ textAlign: "center" }}>AI Translator</h1>

      <div style={{ display: "flex", gap: "1rem", marginTop: "2rem" }}>
        {/* INPUT */}
        <div style={{ flex: 1 }}>
          <p>Detected: {detectedLang || "?"}</p>
          <textarea
            rows={10}
            value={text}
            onChange={(e) => setText(e.target.value)}
            style={{ width: "100%" }}
            placeholder="Enter text..."
          />
        </div>

        {/* OUTPUT */}
        <div style={{ flex: 1 }}>
          <p>Result:</p>
          <div
            style={{
              minHeight: "200px",
              border: "1px solid #ccc",
              padding: "1rem",
            }}
          >
            {result}
          </div>
        </div>
      </div>

      {/* CONTROLS */}
      <div style={{ marginTop: "1rem" }}>
        <select
          value={targetLang}
          onChange={(e) => setTargetLang(e.target.value)}
        >
          <option value="en">English</option>
          <option value="fr">French</option>
          <option value="es">Spanish</option>
          <option value="de">German</option>
        </select>

        <button onClick={handleTranslate} disabled={loading}>
          {loading ? "Translating..." : "Translate"}
        </button>

        <button onClick={handleCopy}>Copy</button>
        <button onClick={handleClear}>Clear</button>
      </div>
    </div>
  );
}

export default App;
