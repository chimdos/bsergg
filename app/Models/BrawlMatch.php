<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class BrawlMatch extends Model
{
    public function games()
    {
        return $this->hasMany(Game::class);
    }
}
