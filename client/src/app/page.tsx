"use client";
import { useRouter, useSearchParams } from "next/navigation";

export default function Home() {
  const query = useSearchParams();
  return (
    <div className="grid place-items-center p-0 lg:p-32 h-screen">
      <div className="border w-full h-full">        
        <h1 className="text-center text-2xl font-bold">Chatbot</h1>
      </div>

    </div>
  );
}
