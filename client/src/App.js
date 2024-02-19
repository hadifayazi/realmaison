import {
  createBrowserRouter,
  createRoutesFromElements,
  Route,
  RouterProvider,
} from "react-router-dom";
import RootLayout from "./hocs/RootLayout";
import { HelmetProvider } from "react-helmet-async";
import PropertiesPage from "./pages/PropertiesPage";
import AboutUs from "./components/AboutUs";
import PropertyDetails from "./components/PropertyDetails";
import HomePage from "./pages/HomePage";
import NotFound from "./pages/NotFound";

const router = createBrowserRouter(
  createRoutesFromElements(
    <Route path="/" element={<RootLayout />}>
      <Route index element={<HomePage />} />
      <Route path="/properties" element={<PropertiesPage />} />
      <Route path="/about" element={<AboutUs />} />
      <Route path="/details/:slug" element={<PropertyDetails />} />
      <Route path="*" element={<NotFound />} />
    </Route>
  )
);

const App = () => {
  return (
    <HelmetProvider>
      <RouterProvider router={router} />
    </HelmetProvider>
  );
};

export default App;
