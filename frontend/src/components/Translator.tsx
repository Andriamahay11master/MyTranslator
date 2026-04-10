import { useState } from "react";

export default function Translator() {
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
    } catch {
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
    <div className="app">
      <h1>AI Translator</h1>

      <div className="container">
        {/* INPUT */}
        <div className="panel">
          <p>
            <strong className="text-bold">Language detected:</strong>{" "}
            {detectedLang || "Not detected"}
          </p>
          <textarea
            rows={10}
            value={text}
            onChange={(e) => setText(e.target.value)}
            placeholder="Enter text..."
          />
        </div>

        {/* OUTPUT */}
        <div className="panel">
          <p className="text-bold">Result:</p>
          <div className="result-box">{result}</div>
        </div>
      </div>

      <div className="controls">
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
