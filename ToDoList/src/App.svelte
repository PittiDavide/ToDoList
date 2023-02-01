<script>
  import { onMount } from "svelte";

  let array = [];
  let content = "";
  onMount(async () => {
    const response = await fetch("http://localhost:8080/tasks");
    const data = await response.json();
    array = data;
  });

  async function addTask() {
    if (!content) return;
    const response = await fetch("http://localhost:8080/tasks", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        content: content,
      }),
    });
    const data = await response.json();
    array = [...array, { content: content, id: data.id, done: false }];
  }

  async function deleteTask(event) {
    const id = event.target.parentNode.querySelector("input").id.substring(8);
    const response = await fetch("http://localhost:8080/tasks/" + id, {
      method: "DELETE",
    });
    const data = await response.json();
    array = array.filter((t) => t.id != id);
  }
</script>

<main>
  <h1>ToDo List</h1>
  <div>
    <input type="text" bind:value={content} placeholder="Add a task" />
    <button on:click={addTask}>Add</button>
  </div>
  <li>
    {#each array as t}
      <ul>
        <input type="checkbox" id="checkbox{t.id}" />
        <label for="checkbox{t.id}">{t.content}</label>
        <button on:click={deleteTask} class="delete-btn">Elimina</button>
      </ul>
    {/each}
  </li>
</main>

<style>
  div {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 20px;
  }

  input[type="text"] {
    width: 70%;
  }
  input[type="checkbox"] {
    display: none;
  }

  label {
    display: block;
    padding: 10px;
    background-color: #eee;
    margin-bottom: 5px;
    border-radius: 10px;
    line-height: 2em;
  }

  label::before {
    content: "\2610";
    font-size: 1.5em;
    display: inline-block;
    margin-right: 5px;
    color: #999;
    transition: all 0.3s ease-in-out;
    vertical-align: middle;
  }

  input[type="checkbox"]:checked + label {
    background-color: #ddd;
  }

  input[type="checkbox"]:checked + label::before {
    content: "\2611";
    color: #333;
  }

  label {
    font-size: 1.2em;
    font-family: Arial, sans-serif;
    cursor: pointer;
  }
  h1 {
    text-align: center;
    font-size: 2em;
    margin: 20px 0;
    font-family: Arial, sans-serif;
  }
  input[type="text"] {
    padding: 10px;
    font-size: 1.2em;
    width: 80%;
    margin: 10px auto;
    display: block;
    margin-right: 10px;
  }
  li {
    list-style: none;
    padding: 0;
    text-align: center;
    align-items: center;
  }
  ul {
    margin: 10px;
    background-color: rgb(76, 71, 71);
    border-radius: 10px;
    padding: 10px;
  }
  .delete-btn {
    background-color: red;
    color: white;
    padding: 5px 10px;
    border-radius: 5px;
    margin-left: 10px;
    cursor: pointer;
  }
</style>
