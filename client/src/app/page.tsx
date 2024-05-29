'use client'

import axios from "axios";
import { useState } from "react";

export default function Home() {

  const [ res, setRes ] = useState('')
  const [ input, setInput ] = useState("")
  const handleGenerateSegitiga = () => {
    if (isNaN(input)){
      setRes("Input harus berupa angka in client")
      setInput("")
      return
    }
    axios.post("http://127.0.0.1:5000/segitiga",{number:input})
      .then((res) =>{
        setRes(res.data.data)
      })
  }

  const handleGenerateBilanganPrima = () => {
    if (isNaN(input)){
      setRes("Input harus berupa angka in client")
      setInput("")
      return
    }
    axios.post("http://127.0.0.1:5000/prima",{max:input})
      .then((res) =>{
        setRes(res.data.data)
    })
  }

  const handleGenerateBilanganGanjil = () => {
    if (isNaN(input)){
      setRes("Input harus berupa angka in client")
      setInput("")
      return
    }
    axios.post("http://127.0.0.1:5000/ganjil",{max:input})
      .then((res) =>{
        console.log(res.data.data);
        
        setRes(res.data.data)
    })
  }

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div className="z-10 w-full max-w-5xl items-center">
        <input type="text" name="angka" id="angka" placeholder="Input angka" onChange={(e) => setInput(e.target.value)} value={input} />
        <div style={{ display: "flex", gap:10, marginTop: 10 }}>
          <button onClick={handleGenerateSegitiga}>Generate Segitiga</button>
          <button onClick={handleGenerateBilanganGanjil}>Generate Bilangan Ganjil</button>
          <button onClick={handleGenerateBilanganPrima}>Generate Bilangan Prima</button>
        </div>
        <h3 className="text-3lg">Result</h3>
        <pre>{res}</pre>
      </div>
    </main>
  );
}
