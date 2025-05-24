// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getFirestore } from "firebase/firestore";
import { getAuth } from "firebase/auth";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAlY5dzjtttgZvRXOi23tPkigLY6HQOI3w",
  authDomain: "dash-ad951.firebaseapp.com",
  projectId: "dash-ad951",
  storageBucket: "dash-ad951.firebasestorage.app",
  messagingSenderId: "450466504856",
  appId: "1:450466504856:web:1b57767277f6ed16f7b0ed",
  measurementId: "G-N0QNQVZL1F"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
// Initialize Analytics
const analytics = getAnalytics(app);
// Initialize Firestore
const db = getFirestore(app);
// Initialize Firebase Authentication and get a reference to the service
const auth = getAuth(app);

export { app, analytics, db, auth };