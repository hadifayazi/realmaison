import { configureStore } from "@reduxjs/toolkit";
import { userApi } from "./apis/user";
import { propertiesApi } from "./apis/properties";
import { setupListeners } from "@reduxjs/toolkit/query";

export const store = configureStore({
  reducer: {
    [userApi.reducerPath]: userApi.reducer,
    [propertiesApi.reducerPath]: propertiesApi.reducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware()
      .concat(userApi.middleware)
      .concat(propertiesApi.middleware),
});

setupListeners(store.dispatch);

export {
  useGetPropertiesQuery,
  useGetRealtorPropertiesQuery,
  useAddPropertyMutation,
  useUpdatePropertyMutation,
  useGetPropertyQuery,
  useDeletePropertyMutation,
  useGetPorpertyDetailsQuery,
} from "./apis/properties";
