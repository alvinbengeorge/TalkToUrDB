"use client";
import { useRouter, useSearchParams } from "next/navigation";
import { useState } from "react";

export default function Home() {
  const query = useSearchParams();
  const session = query.get("session");
  const chats = useState([]);
  return (
    <div className="grid place-items-center p-0 lg:p-32 h-screen">
      
    </div>
  );
}
