import React, { useEffect, useState } from 'react';
import { Card } from './Components/Card/card';
import './App.css';

function App() {
  const [button, setButton] = useState("No Task");
  const [wixiteamData, setWixiteamData] = useState([]);
    const [wixitasksData, setWixitasksData] = useState([]);

  useEffect(() => {
    fetch('/wixiteam')
      .then(response => response.json())
      .then(data => setWixiteamData(data))
      .catch(error => console.error(error));
  }, []);

    useEffect(() => {
    fetch('/wixitasks')
      .then(response => response.json())
      .then(data => setWixitasksData(data))
      .catch(error => console.error(error));
  }, []);

  useEffect(() => {
    if (button === "Login") {
      // handle login logic here
      console.log("Login button clicked");
    } else if (button === "New Task") {
      // handle new task logic here
      console.log("New Task button clicked");
    } else if (button === "Update Task") {
      // handle update task logic here
      console.log("Update Task button clicked");
    } else if (button === "Logout") {
      // handle logout logic here
      console.log("Logout button clicked");
    }
  }, [button]);

  return (
    <div className="App">
        <header></header>
        <div className="container">
              <Card />
              <p></p>
              <div>
              <button onClick={() => setButton("Login")}>Login</button>
              <button onClick={() => setButton("New Task")}>New Task</button>
              <button onClick={() => setButton("Update Task")}>Update Task</button>
              <button onClick={() => setButton("Logout")}>Logout</button>
            </div>
            <h1>Current process is {button}</h1>
            <div>
                <h1>Back End Magic</h1>
                <h3>Wixiteam Data</h3>
                <ul>
                    {wixiteamData.map(item => (
                      <li key={item.emp_id}>
                        {item.first_name} {item.surname} ({item.position}) - {item.department}
                      </li>
                    ))}
                </ul>
            </div>
            <div>
                <h3>Wixitasks Data</h3>
                <ul>
                    {wixitasksData.map(item => (
                      <li key={item.id}>
                        {item.allocated_to} {item.task} ({item.date_allocated}) - {item.description}
                      </li>
                    ))}
                </ul>
            </div>
        </div>
    </div>
  );
}

export default App;