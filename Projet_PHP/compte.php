<?php session_start(); ?> 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <script
      src="https://kit.fontawesome.com/a1b11d373d.js"
      crossorigin="anonymous"
    ></script>
    <title>Document</title>
</head>
<body> 
<div class="bg-white opacity-80 flex-col grid grid-cols-3  shadow overflow-hidden sm:rounded-lg">
  <div class="px-4 py-5 sm:px-6">
    <h3 class="text-lg leading-6 font-medium font-extrabold text-gray-900">
      Mes informations personnelles:
    </h3>
  </div>
  <div class="border-t border-gray-200">
    <dl>
      <div
        class="flex bg-gray-50 px-2 py-5 grid grid-cols-3 gap-4 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6"
      >
        <dt class="text-sm font-medium text-black pt-2 font-bold">Nom :</dt>
        <dd class="mt-1 text-sm text-black pt-1">Bonjour <?php echo $_SESSION['nom']; ?> !</dd>
      </div>
      <hr />
      <div
        class="bg-white flex px-2 py-5 grid grid-cols-3 gap-4 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6"
      >
        <dt class="text-sm pt-2 font-medium text-black font-bold">
          Adresse E-mail:
        </dt>
        <dd class="text-sm pt-2 text-gray-900"></dd>
      </div>
      <hr />
      <div
        class="flex flex-row bg-gray-50 px-2 py-5 grid grid-cols-3 gap-3 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6"
      >
        <div class="text-sm pt-2 font-medium text-black font-bold">
          Adresse:
        </div>
        <div class="mt-1 text-sm pt-1 text-gray-900"></div>
      </div>
    </dl>
    <div>
      <button
    type="submit"
    class="group relative w-full bg-gradient-to-r from-slate-400 to-neutral-900 flex rounded-md justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
  >
  <a  href="index.php?disconnect=0"> Se Déconnecter </a>
  </button>
</div>
  </div>
</div>
  <?php echo $_COOKIE['user_id']; ?>
  <?php echo $_SESSION['login']; ?>
</body>
</html>

