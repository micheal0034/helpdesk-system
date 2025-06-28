import Home from "./pages/Home"

function App() {
  

  return (
    <>
      <Home />
      <footer className="text-center bg-gray-100 text-gray-500 text-sm">
        &copy; {new Date().getFullYear()} Intelligent Help Desk. All rights reserved.
      </footer>
    </>
  )
}

export default App
