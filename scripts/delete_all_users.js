
const { createClient } = require('@supabase/supabase-js');

const SUPABASE_URL = process.env.SUPABASE_URL;
const SUPABASE_SERVICE_KEY = process.env.SUPABASE_SERVICE_KEY;

if (!SUPABASE_URL || !SUPABASE_SERVICE_KEY) {
    console.error("Error: SUPABASE_URL and SUPABASE_SERVICE_KEY must be set.");
    process.exit(1);
}

const supabase = createClient(SUPABASE_URL, SUPABASE_SERVICE_KEY, {
    auth: {
        autoRefreshToken: false,
        persistSession: false
    }
});

async function deleteAllUsers() {
    console.log("Fetching users...");
    const { data: { users }, error } = await supabase.auth.admin.listUsers();

    if (error) {
        console.error("Error fetching users:", error);
        return;
    }

    if (!users || users.length === 0) {
        console.log("No users found to delete.");
        return;
    }

    console.log(`Found ${users.length} users. Deleting...`);

    for (const user of users) {
        const { error: deleteError } = await supabase.auth.admin.deleteUser(user.id);
        if (deleteError) {
            console.error(`Failed to delete user ${user.email}:`, deleteError.message);
        } else {
            console.log(`Deleted user: ${user.email}`);
        }
    }
    console.log("All users deleted.");
}

deleteAllUsers();
