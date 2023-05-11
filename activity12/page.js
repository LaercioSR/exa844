"use client";

import styles from "./page.module.css";
import React from "react";
import { useState } from "react";

function SearchBar({ filterText, onFilterTextChange }) {
  return (
    <form>
      <label>Procure uma mensagem:</label>
      <input
        type="text"
        value={filterText}
        placeholder="Search..."
        onChange={(e) => onFilterTextChange(e.target.value)}
      />
    </form>
  );
}

function FilterableMessageTable({ messages }) {
  const [filterText, setFilterText] = useState("");

  return (
    <SearchBar filterText={filterText} onFilterTextChange={setFilterText} />
  );
}

export default function Home() {
  const [blogMessages, setBlogMessages] = useState([]);

  fetch("https://...")
    .then((response) => response.json())
    .then((data) => {
      setBlogMessages(data);
    });

  return (
    <main className={styles.main}>
      <FilterableMessageTable messages={blogMessages} />
    </main>
  );
}
