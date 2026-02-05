const { Client } = require('pg');
const fs = require('fs');
const path = require('path');

const connectionString = "postgres://postgres:WMHO1uhzRLngn78w@db.kgcdeqsvqneyysubmnch.supabase.co:5432/postgres";

async function resetAndMigrate() {
    console.log("🔌 Connecting to Supabase...");
    const client = new Client({
        connectionString: connectionString,
        ssl: { rejectUnauthorized: false }
    });

    try {
        await client.connect();
        console.log("✅ Connected.");

        // 1. Reset
        console.log("🔥 Resetting Database (Dropping public schema)...");
        // Robust reset: Drop the entire schema and recreate it.
        await client.query('DROP SCHEMA IF EXISTS public CASCADE;');
        await client.query('CREATE SCHEMA public;');
        await client.query('GRANT ALL ON SCHEMA public TO postgres;');
        await client.query('GRANT ALL ON SCHEMA public TO public;');
        console.log("✅ Database Reset Complete (Schema Recreated).");

        // 2. Migrate
        console.log("🚀 Applying Migrations...");
        const migrationSqlPath = path.join(__dirname, '../supabase/migrations/20260130_full_sync.sql');
        if (fs.existsSync(migrationSqlPath)) {
            const migrationSql = fs.readFileSync(migrationSqlPath, 'utf8');
            await client.query(migrationSql);
            console.log("✅ Migration Applied.");
        } else {
            throw new Error("No migration file found at " + migrationSqlPath);
        }

    } catch (err) {
        console.error("❌ Error:", err);
        process.exit(1);
    } finally {
        await client.end();
    }
}

resetAndMigrate();
