import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Plane, UploadCloud } from "lucide-react";
import { useState } from "react";

function App() {
  const [fileName, setFileName] = useState("Nenhum arquivo selecionado");
  const [file, setFile] = useState<File | null>(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const selectedFile = e.target.files?.[0];
    setFile(selectedFile || null);
    setFileName(selectedFile ? selectedFile.name : "Nenhum arquivo selecionado");
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!file) {
      alert("Selecione um arquivo primeiro.");
      return;
    }

    setLoading(true);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("http://localhost:8000/api/predict", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) throw new Error("Erro ao enviar o arquivo");

      const blob = await response.blob();
      const downloadUrl = window.URL.createObjectURL(blob);

      const a = document.createElement("a");
      a.href = downloadUrl;
      a.download = "resultado.zip";
      a.click();
      window.URL.revokeObjectURL(downloadUrl);
    } catch (err) {
      console.error(err);
      alert("Falha ao enviar o arquivo. Tente novamente.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-zinc-900 flex flex-col">
      <header className="flex items-center gap-3 p-6 border-b border-zinc-700">
        <Plane className="h-10 w-10 text-blue-500" />
        <h1 className="text-4xl font-extrabold text-white tracking-tight">Flight Price</h1>
      </header>

      <main className="flex flex-col flex-grow justify-center items-center px-6">
        <h2 className="text-3xl text-white mb-8 font-semibold">Treine Seu Modelo</h2>

        <form
          onSubmit={handleSubmit}
          className="bg-zinc-800 rounded-3xl shadow-xl p-10 w-full max-w-md flex flex-col gap-6"
        >
          <Label htmlFor="fileInput" className="text-gray-300 font-medium">
            {fileName}
          </Label>

          <Input
            id="fileInput"
            type="file"
            accept=".xlsx,.xls"
            onChange={handleFileChange}
            className="cursor-pointer text-gray-200"
            disabled={loading}
          />

          <Button
            type="submit"
            className="w-full flex justify-center items-center gap-2 border-2 border-blue-500 bg-blue-600 hover:bg-blue-700 active:bg-blue-800 disabled:opacity-50"
            disabled={loading}
          >
            <UploadCloud className="h-5 w-5" />
            {loading ? "Enviando..." : "Treinar"}
          </Button>
        </form>
      </main>
    </div>
  );
}

export default App;
