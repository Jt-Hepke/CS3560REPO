import { Routes, Route, Link } from "react-router-dom"
import Resume from "./pages/resume"
import Projects from "./pages/projects"
import Contact from "./pages/contact"

function App() {
  return (
    <div>

      <h1>John Hepke</h1>

      {/* Navigation Buttons */}
      <nav>
        <Link to="/">Home</Link> |{" "}
        <Link to="/resume">Resume</Link> |{" "}
        <Link to="/projects">Projects</Link> |{" "}
        <Link to="/contact">Contact</Link>
      </nav>

      <hr />

      {/* Page Routes */}
      <Routes>
        <Route path="/" element={<h2>Welcome to my website</h2>} />
        <Route path="/resume" element={<Resume />} />
        <Route path="/projects" element={<Projects />} />
        <Route path="/contact" element={<Contact />} />
      </Routes>

    </div>
  )
}

export default App