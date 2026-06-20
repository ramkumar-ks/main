import React, {useState, useEffect} from "react";

function App() {

  const [data, setData] = useState(null);
  const [id, setId] = useState("");
  const [name, setName] = useState("");
  const [dept, setDept] = useState("");
  const [salary, setSalary] = useState("");

  useEffect(() => {
    fetch('http://127.0.0.1:5000/').
    then((res) => res.json()).
    then((result) => setData(result)).
    catch((err) => console.error("Error:", err))
    },
  []);

  const addItem = () =>  {
    const item = { id, name, department: dept, salary };

    fetch("http://127.0.0.1:5000/add_employee", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(item),
    })
      .then((res) => res.json())
      .then((result) => {
        // backend returns: { result: 'Record inserted' } or { result: 'Insertion failed' }
        console.log("POST response:", result);

        // SIMPLE beginner logic: just show response message in the list area
        setData([{ name: result.result }]);
      })
      .catch((err) => console.error("Error:", err));

    setId("");
    setName("");
    setDept("");
    setSalary("");
  };


return (
  <div>
    <div style={{ marginBottom: 12 }}>
      <input
        placeholder="id"
        value={id}
        onChange={(e) => setId(e.target.value)}
      />
      <input
        placeholder="name"
        value={name}
        onChange={(e) => setName(e.target.value)}
        style={{ marginLeft: 8 }}
      />
      <input
        placeholder="department"
        value={dept}
        onChange={(e) => setDept(e.target.value)}
        style={{ marginLeft: 8 }}
      />
      <input
        placeholder="salary"
        value={salary}
        onChange={(e) => setSalary(e.target.value)}
        style={{ marginLeft: 8 }}
      />

      <button onClick={addItem} style={{ marginLeft: 8 }}>
        Add Employee
      </button>
    </div>

    {
      data &&
        Array.isArray(data) &&
        data.map((item, i) => <div key={i}>{item.name}, {item.department_id}</div>)
    }
  </div>
);
};

export default App;





// import React, {useState, useEffect} from "react";

// function App() {
//   const [data, setData] = useState(null);
//   useEffect(()=>{
//     fetch("http://127.0.0.1:5000")
//     .then((res)=>res.json())
//     .then((result)=>setData(result))
//     .catch((err) => console.error("Error:", err));
//   },[]);

//   return (
//     <div>
//       <h1>Cricket players list</h1>
//       {data ? (
//         <div>
//           <ul>
//             {Array.isArray(data) &&
//               data.map((item, i) => (
//                 <li key={i}>                               
//                   {item.player_name} - {item.played_team}
//                 </li>
//               ))}
//           </ul>
//         </div>
//       ) : (
//         <p>Loading data...</p>
//       )}
//     </div>
//   );
// }

// export default App;





// import React, { useEffect, useState } from "react";

// function App() {
//   const [users, setUsers] = useState([]);

//   const [name, setName] = useState("");
//   const [age, setAge] = useState("");
//   const [role, setRole] = useState("");
//   const [error, setError] = useState("");
//   const [loading, setLoading] = useState(false);

//   const fetchUsers = async () => {
//     const res = await fetch("http://127.0.0.1:5000");
//     const data = await res.json();

//     // backend returns an object for GET `/` (a single user fields object)
//     // and returns an array for POST `/addUser`.
//     if (Array.isArray(data)) {
//       setUsers(data);
//       return;
//     }

//     setUsers([data]);
//   };

//   useEffect(() => {
//     fetchUsers().catch(console.error);
//   }, []);

//   const handleAddUser = async (e) => {
//     e.preventDefault();
//     setError("");

//     // Basic validation
//     const parsedAge = Number(age);
//     if (!name.trim()) return setError("Name is required");
//     if (!Number.isFinite(parsedAge)) return setError("Age must be a number");
//     if (!role.trim()) return setError("Role is required");

//     setLoading(true);
//     try {
//       const res = await fetch("http://127.0.0.1:5000/addUser", {
//         method: "POST",
//         headers: {
//           "Content-Type": "application/json",
//         },
//         body: JSON.stringify({
//           Name: name,
//           Age: parsedAge,
//           Role: role,
//         }),
//       });

//       if (!res.ok) {
//         throw new Error(`POST /addUser failed with status ${res.status}`);
//       }

//       // backend returns `all_users` array
//       await res.json();

//       // refresh list using GET endpoint (simple & consistent)
//       await fetchUsers();

//       setName("");
//       setAge("");
//       setRole("");
//     } catch (err) {
//       console.error(err);
//       setError(err?.message ?? "Failed to add user");
//     } finally {
//       setLoading(false);
//     }
//   };

//   return (
//     <>
//       <h1>Users</h1>

//       <form onSubmit={handleAddUser} style={{ marginBottom: 16 }}>
//         <div>
//           <label>
//             Name:
//             <input
//               value={name}
//               onChange={(e) => setName(e.target.value)}
//               type="text"
//               style={{ marginLeft: 8 }}
//             />
//           </label>
//         </div>

//         <div style={{ marginTop: 8 }}>
//           <label>
//             Age:
//             <input
//               value={age}
//               onChange={(e) => setAge(e.target.value)}
//               type="number"
//               style={{ marginLeft: 8 }}
//             />
//           </label>
//         </div>

//         <div style={{ marginTop: 8 }}>
//           <label>
//             Role:
//             <input
//               value={role}
//               onChange={(e) => setRole(e.target.value)}
//               type="text"
//               style={{ marginLeft: 8 }}
//             />
//           </label>
//         </div>

//         <button type="submit" disabled={loading} style={{ marginTop: 12 }}>
//           {loading ? "Adding..." : "Add User"}
//         </button>

//         {error ? <p style={{ color: "red" }}>{error}</p> : null}
//       </form>

//       {users.map((user, idx) => (
//         <div key={idx} style={{ marginBottom: 8 }}>
//           <p>
//             <strong>Name:</strong> {user?.Name}
//           </p>
//           <p>
//             <strong>Age:</strong> {String(user?.Age)}
//           </p>
//           <p>
//             <strong>Role:</strong> {user?.Role}
//           </p>
//         </div>
//       ))}
//     </>
//   );
// }

// export default App;


