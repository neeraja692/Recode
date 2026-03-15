# SecureComm - Internal Messaging Platform

> A role-based, real-time internal messaging system built for distributed engineering organizations who need full control over their communication infrastructure.

---

## Problem Statement

Organizations rarely trust external communication platforms with sensitive internal conversations. Instead they need to build their own. SecureComm allows messages to travel instantly between rooms, teams, and individuals while enforcing a strict hierarchy of roles and permissions. Unlike public chat apps, not everyone holds equal power in SecureComm.

---

## What We Built

SecureComm is a self-hosted, lightweight internal messaging platform that solves the following:

- Someone holds ultimate authority over the entire system (Admin)
- Certain users can create and manage discussion rooms (Moderator)
- Others can only participate in conversations (Member)
- Messages travel instantly between all connected clients
- The platform responds to commands when special inputs are detected

---

## Pages and What Each One Does

### Cover Page - `coverpage.html`
The landing page of the platform. Displays the SecureComm logo with a floating animation on a beige background. Has a single Start button that takes the user to the Sign Up page. This is the first screen anyone sees when they open the app.

### Sign Up - `signup.html`
Allows new users to register by entering their name, username, password, and selecting a role. On successful signup the user is immediately redirected to their role-based dashboard. If the username already exists the system shows an error.

### Login - `login.html`
The authentication page where users enter their username, password, and select their role. The backend verifies all three must match. On success the user is redirected to the correct dashboard. On failure the system shows an invalid credentials message.

| Role Selected | Redirects To |
|---|---|
| Admin | `admin.html` |
| Moderator | `moderator.html` |
| Member | `follow.html` |

### Admin Dashboard - `admin.html`
The control panel for the Admin. Receives and displays a live log of all admin actions performed in the system. Actions are recorded in memory and passed from the backend to the page on every load.

### Moderator Dashboard - `moderator.html`
The dashboard for Moderators. Can create and manage rooms and moderate users within their assigned rooms. Cannot access system-level controls reserved for Admin.

### Member Page - `follow.html`
The main page for regular Members. Split into two sections:

Left Sidebar:
- Shows a Follow Pages list with three user profiles - Sarah Johnson (Marketing Manager), David Lee (Software Engineer), and Priya Sharma (Product Designer)
- Each profile has a Follow button. Once clicked the button changes to Followed and gets disabled
- Following a user instantly opens a private chat window on the right side
- Shows an active Room: Manju Patil card displaying chat status and 30 joined members
- Room card has a Join button to enter the group chat

Right Chat Area:
- Default state shows an Explore screen
- When a user is followed a private chat opens showing previous messages and a live input box
- When Join is clicked a group chat opens with existing messages and an Exit button in the header
- Clicking Exit returns to the Explore screen and re-enables the Join button
- All sent messages auto-scroll to the bottom and appear instantly

---

## Role and Permission System

| Action | Member | Moderator | Admin |
|---|---|---|---|
| Send and receive messages | Yes | Yes | Yes |
| Join and leave rooms | Yes | Yes | Yes |
| Follow users and private chat | Yes | Yes | Yes |
| Exit a group room | Yes | Yes | Yes |
| Create a new room | No | Yes | Yes |
| Delete a room | No | Own only | Yes |
| Kick a user | No | Yes | Yes |
| Mute a user | No | Yes | Yes |
| Assign roles | No | No | Yes |
| Delete any user | No | No | Yes |
| Shutdown system | No | No | Yes |

---

## Built-in Commands

```
/rooms              - List all available rooms
/join <room>        - Join a specific room
/leave <room>       - Leave current room
/kick <username>    - Remove user from room     [Moderator+]
/mute <username>    - Silence a user            [Moderator+]
/promote <username> - Elevate user role         [Admin only]
/shutdown           - Graceful system shutdown  [Admin only]
```

---

## User Flow

```
coverpage.html
      |
      v (Click Start)
  signup.html
      |
      v (Have account? Login)
  login.html --> Select Role
      |
      |-- Admin      -->  admin.html
      |-- Moderator  -->  moderator.html
      └-- Member     -->  follow.html
                              |
                    |---------+----------|
                    v                    v
             Follow a user          Join a Room
                    |                    |
             Private chat         Group chat opens
             window opens         with Exit button
```

---

## Project Structure

```
securecomm/
├── templates/
│   ├── coverpage.html        - Landing page with Start button
│   ├── signup.html           - User registration page
│   ├── login.html            - Login with role selection dropdown
│   ├── admin.html            - Admin dashboard with action logs
│   ├── moderator.html        - Moderator room management dashboard
│   └── follow.html           - Member follow, private chat and group room
├── users.txt
│── follow_data.txt          
└── app.py                    - Flask server with all routes and logic
```
