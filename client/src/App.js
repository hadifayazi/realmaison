import {
  createBrowserRouter,
  createRoutesFromElements,
  Route,
  RouterProvider,
} from "react-router-dom";
import RootLayout from "./hocs/RootLayout";
import PropertyList from "./components/PropertyList";
import AboutUs from "./components/AboutUs";
import PropertyDetails from "./components/PropertyDetails";

const router = createBrowserRouter(
  createRoutesFromElements(
    <Route path="/" element={<RootLayout />}>
      <Route index element={<PropertyList />} />,
      <Route path="/about" element={<AboutUs />} />,
      <Route path="/details/:slug" element={<PropertyDetails />} />,
      {/* <Route path="*" element={<NotFound />} /> */}
    </Route>
  )
);

const App = () => {
  return <RouterProvider router={router} />;
};

export default App;
