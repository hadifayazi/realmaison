import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const userApi = createApi({
  reducerPath: "userApi",
  baseQuery: fetchBaseQuery({
    baseUrl: "http://127.0.0.1:8000/api/v1/auth/",
  }),
  endpoints: (builder) => ({
    signup: builder.mutation({
      query: (user) => {
        return {
          url: "users/",
          method: "POST",
          body: {
            user: { user },
          },
        };
      },
    }),
    login: builder.mutation({
      query: ({ email, password }) => {
        return {
          url: "jwt/create/",
          method: "POST",
          body: {
            email: email,
            password: password,
          },
        };
      },
    }),
    // activationAccount: builder.mutation,
  }),
});
