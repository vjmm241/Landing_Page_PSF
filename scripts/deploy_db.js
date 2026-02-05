const { Client } = require('pg');
const fs = require('fs');
const path = require('path');

// Credentials (Hardcoded for this execution based on USER request)
const connectionString = "postgres://postgres.kgcdeqsvqneyysubmnch:WMHO1uhzRLngn78w@aws-0-eu-central-1.pooler.supabase.com:6543/postgres";
// Note: connection string format is standard Supabase: postgres://postgres.[ref]:[pass]@[host]:6543/postgres
// I am inferring the host closer to standard. If this fails, I will try the direct db... format.
// Ref: kgcdeqsvqneyysubmnch.
// Pass: WMHO1uhzRLngn78w
// Standard host: db.kgcdeqsvqneyysubmnch.supabase.co
// Transaction Pooler is usually port 6543 or 5432.
// Let's try the direct connection URL first which is safer if pooler is not set up.
const directUrl = "postgres://postgres:WMHO1uhzRLngn78w@db.kgcdeqsvqneyysubmnch.supabase.co:5432/postgres";

async function migrate() {
    console.log("🔌 Conectando a Supabase...");
    const client = new Client({
        connectionString: directUrl,
        ssl: { rejectUnauthorized: false }
    });

    try {
        await client.connect();
        console.log("✅ Conexión establecida.");

        const sqlPath = path.join(__dirname, '../docs/SCHEMA_SUPABASE.sql');
        const sql = fs.readFileSync(sqlPath, 'utf8');

        console.log("🚀 Ejecutando SQL...");
        await client.query(sql);
        console.log("✅ Migración completada con éxito.");

    } catch (err) {
        console.error("❌ Error en migración:", err);
    } finally {
        await client.end();
    }
}

migrate();
